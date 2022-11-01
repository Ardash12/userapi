from django.urls import path


from .views import UserGetApi, UserRegisterApi, UserLoginApi


urlpatterns = [
    path('user/', UserGetApi.as_view()),
    path('auth/register/', UserRegisterApi.as_view()),
    path('auth/login/', UserLoginApi.as_view()),
]
