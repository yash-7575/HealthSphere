from django.urls import path
from . import views
from .views import send_test_email

urlpatterns = [
    path('', views.Home, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('login1/', views.LoginView, name='login1'),
    path('logout1/', views.LogoutView, name='logout1'),
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name='reset-password'),
    path('send-email/', send_test_email, name='send_email'),
]