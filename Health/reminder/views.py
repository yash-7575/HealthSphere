from django.shortcuts import render
from django.http import JsonResponse
import pyttsx3
import threading
import time

# Global variables
reminder_thread = None
reminder_active = False
tts_engine = None

# Initialize TTS engine globally
def init_tts():
    global tts_engine
    tts_engine = pyttsx3.init()
    tts_engine.setProperty('rate', 150)  # Set speech rate

def speak(text):
    global tts_engine
    if tts_engine is None:
        init_tts()
    tts_engine.say(text)
    tts_engine.runAndWait()

def reminder_loop(username, interval):
    global reminder_active
    while reminder_active:
        speak(f"Hey {username}, drink water!")
        time.sleep(interval)

def start_reminder(request):
    global reminder_thread, reminder_active

    if request.method == "GET":
        username = request.GET.get("username", "User")
        interval_seconds = int(request.GET.get("interval_seconds", 0))
        interval_minutes = int(request.GET.get("interval_minutes", 0))
        interval_hours = int(request.GET.get("interval_hours", 0))

        interval = interval_seconds + (interval_minutes * 60) + (interval_hours * 3600)

        if interval <= 0:
            return JsonResponse({"error": "Invalid interval time!"}, status=400)

        if not reminder_active:  # Start only if not running
            reminder_active = True
            reminder_thread = threading.Thread(target=reminder_loop, args=(username, interval), daemon=True)
            reminder_thread.start()

        return JsonResponse({"status": "Reminder started", "user": username, "interval_seconds": interval_seconds, "interval_minutes": interval_minutes, "interval_hours": interval_hours})

    return JsonResponse({"error": "Invalid request"}, status=400)

def stop_reminder(request):
    global reminder_active
    reminder_active = False  # Stop the loop
    return JsonResponse({"status": "Reminder stopped"})

def hydration_reminders(request):
    return render(request, "reminder/reminder.html")
