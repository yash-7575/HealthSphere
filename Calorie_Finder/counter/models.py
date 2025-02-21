
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Table for storing food search history
class FoodHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=255)
    calories = models.IntegerField()
    carbohydrates = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_name} - {self.user.username}"
