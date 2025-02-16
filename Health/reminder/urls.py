from django.urls import path
from reminder.views import hydration_reminders, start_reminder, stop_reminder

urlpatterns = [
    path('', hydration_reminders, name='hydration_reminders'),
    path('start/', start_reminder, name='start_reminder'),
    path('stop/', stop_reminder, name='stop_reminder'),
]
