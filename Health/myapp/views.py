from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import os
from dotenv import load_dotenv
from .models import *

load_dotenv()

# Basic Page Views
def home(request):
    return render(request, 'main_index.html')

def ai_assistant(request):
        return render(request, 'ai_assistant.html')

# def calorie_finder(request):
#     return render(request, 'calorie_finder.html')

def features(request):
    return render(request, 'features.html')

def daily_planner(request):
    return render(request, 'daily_planner.html')

# def hydration_reminders(request):
#     return render(request, 'hydration_reminders.html')

# def community(request):
    # return render(request, 'community.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def error_404(request):
    return render(request, '404.html')

def features(request):
    return render(request, 'features.html')

def categories(request):
    return render(request, 'categories.html')

def exercise(request):
    return render(request, 'exercise.html')

def tracking(request):
    return render(request, 'tracking.html')

def interactive(request):
    return render(request, 'interactive.html')

def articles_and_resources(request):
    return render(request, 'articles_and_resources.html')

def contact(request):
    return render(request, 'contact.html')

def meditation(request):
    return render(request, 'meditation.html')

def join(request):
    return render(request, 'join.html')

def sleep(request):
    return render(request, 'sleep.html')

def mindfulness(request):
    return render(request, 'mindfulness.html')

def mental_health(request):
    return render(request, 'mental_health.html')

def plans(request):
    return render(request, 'plans.html')

def for_business(request):
    return render(request, 'for_business.html')

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

# Authentication Views
# @login_required
# def index2(request):
#     return render(request, 'index2.html')

# def RegisterView(request):
#     if request.method == "POST":
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user_data_has_error = False

#         if User.objects.filter(username=username).exists():
#             user_data_has_error = True
#             messages.error(request, "Username already exists")

#         if User.objects.filter(email=email).exists():
#             user_data_has_error = True
#             messages.error(request, "Email already exists")

#         if len(password) < 5:
#             user_data_has_error = True
#             messages.error(request, "Password must be at least 5 characters")

#         if user_data_has_error:
#             return redirect('register')
#         else:
#             new_user = User.objects.create_user(
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=email, 
#                 username=username,
#                 password=password
#             )
#             messages.success(request, "Account created. Login now")
#             return redirect('login')

#     return render(request, 'register.html')

# def LoginView(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('index2')
#         else:
#             messages.error(request, "Invalid login credentials")
#             return redirect('login')

#     return render(request, 'login.html')

# def LogoutView(request):
#     logout(request)
#     return redirect('login')

# AI API Views
# def ai_index(request):
#     return render(request, 'index.html')
