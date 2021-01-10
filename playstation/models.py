from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    fullname = models.CharField(blank=True, max_length=150)
    nickname = models.CharField(blank=True, max_length=150) 
    email = models.CharField(blank=True, max_length=150)
    