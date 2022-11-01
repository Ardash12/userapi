from django.urls import path


from .views import UserViewset, UserApi, UserRegister


urlpatterns = [
    path('user/', UserApi.as_view()),
    path('auth/register/', UserRegister.as_view()),
]
