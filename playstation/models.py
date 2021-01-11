from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    fullname = models.CharField(blank=True, max_length=150)
    nickname = models.CharField(blank=True, max_length=150) 
    email = models.CharField(blank=True, max_length=150)
    
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.
class User(AbstractUser):
   profile_pic= CloudinaryField('image')
   contact = models.IntegerField(null=True)
