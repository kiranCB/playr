from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

USER = settings.AUTH_USER_MODEL

# Create your models here.
class CustomUser(AbstractUser):
    pass

# Location model

class LocationModel(models.Model):
    lattitude = models.FloatField()
    longitude = models.FloatField()
    

    def __str__(self):
        return f"{self.lattitude},{self.longitude}"

# Profile Model
class ProfileModel(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("T", "Transgender"),
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)    
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to="user/profile/image/", default="default/user.png")
    phone_number = models.CharField(max_length=15)
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".title()