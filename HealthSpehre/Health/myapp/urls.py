from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('exercise/', views.exercise, name='exercise'),
    path('category01/', views.category01, name='category01'),
    path('category02/', views.category02, name='category02'),
    path('category03/', views.category03, name='category03'),
    path('category04/', views.category04, name='category04'),
    path('home/', views.home, name='home'),
    path('articles-and-resources/', views.articles_and_resources, name='articles_and_resources'),
    path('meditation/', views.meditation, name='meditation'),
    path('sleep/', views.sleep, name='sleep'),
    path('mindfulness/', views.mindfulness, name='mindfulness'),
    path('mental-health/', views.mental_health, name='mental_health'),
    path('plans/', views.plans, name='plans'),
    path('for-business/', views.for_business, name='for_business'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    # Authentication
    path('login/', views.LoginView, name='login'),
    path('register/', views.RegisterView, name='register'),
    path('index2/', views.index2, name='index2'),
    path('logout/', views.LogoutView, name='logout'),
    # API
    path('generate/', views.generate_response, name='generate'),
    path('ai_index/', views.ai_index, name='ai_index'),
]