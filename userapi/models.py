from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    name = models.CharField(max_length=64, blank=False)
    birth = models.DateField(blank=False)
    phone = models.CharField(max_length=12, blank=False)
    tg = models.CharField(max_length=64, blank=False)

