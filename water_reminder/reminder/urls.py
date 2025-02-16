from django.urls import path
from .views import home, start_reminder

urlpatterns = [
    path('', home, name='home'),
    path('start/', start_reminder, name='start_reminder'),
]
