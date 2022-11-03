import datetime

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet
from rest_framework.response import Response

from drf_standardized_errors.handler import exception_handler

from .serializers import UserRegisterSerializer, UserLoginSerializer, UserGetSerializer
from .models import User


class UserGetApi(APIView):
    '''GET API
    Класс получения данных пользователя по ID
    с помощью query параметра "id"'''

    def get(self, request):
        user_id = request.query_params['id']
        user = User.objects.get(id=user_id)
        return Response(UserRegisterSerializer(user).data)

    # def get_exception_handler(self):
    #     '''Добавьте этот метод, если хотите сами выбрать классы, 
    #     которые будут использовать модуль drf_standardized_errors,
    #     Также необходимо закомментировать строку "EXCEPTION_HANDLER" 
    #     из REST_FRAMEWORK в файле settings.py'''
    #     return exception_handler


class UserLoginApi(APIView):
    '''POST API
    Класс авторизации'''

    serializer_class = UserLoginSerializer

    @csrf_exempt
    def post(self, request):
        if User.objects.filter(username=request.data['username'], password=request.data['password']).exists():
            id = User.objects.get(username=request.data['username']).id
            return Response({'id': id}, status=200)
        else:
            return Response({'code': 401, 'detail': 'Неверный логин или пароль'}, status=401)


class UserRegisterApi(APIView):
    '''POST API 
    Класс регистрации пользователя,
    перед обработкой запроса идет проверка на совершеннолетие'''

    serializer_class = UserRegisterSerializer

    @csrf_exempt
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

        

    