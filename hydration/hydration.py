import pyttsx3
import tkinter
from tkinter import messagebox
import time

a = input("Enter your name :")
seconds = int(input("After how many seconds you want this application to send remainder again ? "))
repeating_time = seconds

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change the index to select a different voice
    engine.say(text)
    engine.runAndWait()

def display_alert(title, message):
    b = tkinter.Tk()
    b.withdraw()
    messagebox.showinfo(title, message)

while True:
    speak(f"hey {a} , drink water!")
    display_alert(f"For {a}", "Drink water!")
    time.sleep(repeating_time)