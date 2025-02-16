from django.shortcuts import render
from django.http import JsonResponse
import pyttsx3
import time
import threading

# Global variables
reminder_thread = None
reminder_active = False

def speak(text):
    """Speaks text using pyttsx3."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def reminder_loop(username, interval):
    """Loop to remind user to drink water."""
    global reminder_active
    while reminder_active:
        speak(f"Hey {username}, drink water!")  # Text-to-speech
        time.sleep(interval)  # Wait for the next reminder

def start_reminder(request):
    """Starts the reminder thread."""
    global reminder_thread, reminder_active

    if request.method == "GET":
        username = request.GET.get("username", "User")
        interval = int(request.GET.get("interval", 60))  # Default: 60 seconds

        if not reminder_active:
            reminder_active = True
            reminder_thread = threading.Thread(target=reminder_loop, args=(username, interval), daemon=True)
            reminder_thread.start()

        return JsonResponse({"status": "Reminder started", "user": username, "interval": interval})

    return JsonResponse({"error": "Invalid request"}, status=400)

def stop_reminder(request):
    """Stops the reminder thread."""
    global reminder_active
    reminder_active = False  # This stops the loop
    return JsonResponse({"status": "Reminder stopped"})

def hydration_reminders(request):
    """Renders the HTML page."""
    return render(request, "reminder/reminder.html")
