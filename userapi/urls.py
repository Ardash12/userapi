from django.urls import path, include
from rest_framework import routers

from .views import UserGetApi, UserRegisterApi, UserLoginApi


urlpatterns = [
    path('user/', UserGetApi.as_view()),
    path('auth/register/', UserRegisterApi.as_view()),
    path('auth/login/', UserLoginApi.as_view()),
]
