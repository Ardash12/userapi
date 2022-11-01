import datetime
from urllib import response

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from .serializers import UserSerializer
from .models import User


class UserLoginApi(APIView):
    def post(self, request):
        try:
            username = request.data['login']
            password = request.data['password']

            if User.objects.filter(username=username, password=password).exists():
                id = User.objects.get(username=username).id
                return Response({'id': id}, status=200)
            else:
                return Response({'code': 401, 'detail': 'Неверный логин или пароль'}, status=401)
        except Exception as e:
            print('Ошибка', e)
            return Response({'code': 400, 'detail': 'Ошибка в передаваемом JSON'}, status=400)


class UserRegisterApi(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        try:
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
        except Exception as e:
            print('Ошибка', e)
            return Response({'code': 400, 'detail': 'Ошибка в передаваемом JSON'}, status=400)

class UserGetApi(APIView):
    def get(self, request):
        try:
            user_id = request.GET['id']
            user = User.objects.get(id=user_id)
            # exc = APIException()

            n = User.objects.filter(birth='1981-10-31').exists()
            print(n)

            return Response(
                {
                    'phone': user.phone,
                    'username': user.username,
                    'name': user.name,
                    'birth': user.birth,
                    'email': user.email,
                    'tg': user.tg,
                }
            )
        except Exception as e:
            
            
            print('Ошибка', e)
            return Response({'errors': str(e)}, status=400)
            

    