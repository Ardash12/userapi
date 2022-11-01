from rest_framework import serializers
from .models import User


# class UserGetSerializer(serializers.Serializer):
#     class Meta:
#         model = User
#         fields = [
#             'phone',
#             'username',
#             'name',
#             'birth',
#             'email',
#             'tg',
#         ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
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
