from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    text = models.CharField(max_length=255)
    calories = models.IntegerField(null=True, blank=True)
    total_calories = models.BooleanField(default=False)
