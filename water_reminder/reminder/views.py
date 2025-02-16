from django.shortcuts import render
from django.http import JsonResponse
import pyttsx3
import threading
import time

# Global variables for reminder
reminder_thread = None
reminder_active = False

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def reminder_loop(username, interval):
    global reminder_active
    while reminder_active:
        speak(f"Hey {username}, drink water!")
        time.sleep(interval)

def start_reminder(request):
    global reminder_thread, reminder_active

    if request.method == "GET":
        username = request.GET.get("username", "User")
        interval = int(request.GET.get("interval", 60))  # Default 60 seconds

        if not reminder_active:  # Only start if not already running
            reminder_active = True
            reminder_thread = threading.Thread(target=reminder_loop, args=(username, interval))
            reminder_thread.daemon = True
            reminder_thread.start()

        return JsonResponse({"status": "Reminder started", "user": username, "interval": interval})

    return JsonResponse({"error": "Invalid request"}, status=400)

def stop_reminder(request):
    global reminder_active
    reminder_active = False  # Stop the loop
    return JsonResponse({"status": "Reminder stopped"})

def home(request):
    return render(request, "reminder/reminder.html")
