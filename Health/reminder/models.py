from django.db import models

class Reminder(models.Model):
    username = models.CharField(max_length=100)
    interval = models.IntegerField(default=60)  # Default: 60 seconds
