from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    mail = models.EmailField(default="test@example.com")
    phone = models.CharField(max_length= 8)
    password = models.CharField(max_length= 255)
    image = models.CharField(max_length= 1000, null=True)


    def __str__(self):
        return self.username
