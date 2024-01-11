from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    password = models.CharField(max_length=128, default="12345678")
    username = models.CharField(max_length=32, unique=True, null=True)
