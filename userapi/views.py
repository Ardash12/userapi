import datetime

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User


class UserRegister(APIView):
    def post(self, request):
        birth = datetime.datetime.strptime(request.data['birth'], '%Y-%m-%d').date()
        today = datetime.date.today()
        age = today.year - birth.year
        if age >= 18:
            user_new = User.objects.create(
                phone = request.data['phone'],
                username = request.data['login'],
                password = request.data['password'],
                name = request.data['name'],
                birth = birth,
                email = request.data['email'],
                tg = request.data['tg'],
            )
            return Response({'id': user_new.id})
        else:
            return Response({'denied': 'Регистрация доступна только для совершеннолетних'})


class UserApi(APIView):
    def get(self, request):
        user_id = request.GET['id']
        user = User.objects.get(id=user_id)
        phone = user.phone
        username = user.username
        name = user.name
        birth = user.birth
        email = user.email
        tg = user.tg

        today = datetime.date.today()
        print(today)
        print(today.year - birth.year)
        print(Response)
        return Response(
            {
                'phone': phone,
                'username': username,
                'name': name,
                'birth': birth,
                'email': email,
                'tg': tg,
            }
        )


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# def user_get(request):
#     id_user = request.query_params['id']
#     id_user = request.GET['id']
#     print(id_user)
#     return HttpResponse(request)
    