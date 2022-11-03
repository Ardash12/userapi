from dataclasses import field
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import User


class UserGetSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone',
            'username',
            'name',
            'birth',
            'email',
            'tg',
        ]


class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone',
            'username',
            'password',
            'name',
            'birth',
            'email',
            'tg',
        ]
