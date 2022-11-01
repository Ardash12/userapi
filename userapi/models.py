from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''Поменять blank='''
    name = models.CharField(max_length=64, blank=True)
    birth = models.DateField(blank=False)
    phone = models.CharField(max_length=12, blank=True)
    tg = models.CharField(max_length=64, blank=True)

