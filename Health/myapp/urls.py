from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('meditation/', views.meditation, name='meditation'),
    path('mindfulness/', views.mindfulness, name='mindfulness'),
    path('mental-health/', views.mental_health, name='mental_health'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    # Authentication
    # path('login/', views.LoginView, name='login'),
    # path('register/', views.RegisterView, name='register'),
    # path('index2/', views.index2, name='index2'),
    # path('logout/', views.LogoutView, name='logout'),
    # API
    # path('generate/', views.generate_response, name='generate'),
    # path('ai_index/', views.ai_index, name='ai_index'),
    # path('ai_login/', views.ai_login, name='ai_login'),
    path('ai_assistant/', views.ai_assistant, name='ai_assistant'),
    # path('calorie_finder/', views.calorie_finder, name='calorie_finder'),
    path('daily_planner/', views.daily_planner, name='daily_planner'),
    # path('hydration_reminders/', views.hydration_reminders, name='hydration_reminders'),
    # path('community/', views.community, name='community'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('404/', views.error_404, name='404'),
    path('features/', views.features, name='features'),
    path('tracking/', views.tracking, name='tracking'),
    path('interactive/', views.interactive, name='interactive'),
    path('contact/', views.contact, name='contact'),
    path('join/', views.join, name='join'),
]