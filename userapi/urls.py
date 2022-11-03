from django.urls import path, include
from rest_framework import routers

from .views import UserGetApi, UserRegisterApi, UserLoginApi


urlpatterns = [
    path('v1/user/', UserGetApi.as_view()),
    path('v1/auth/register/', UserRegisterApi.as_view()),
    path('v1/auth/login/', UserLoginApi.as_view()),
]
