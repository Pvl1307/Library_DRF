from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterUserAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register_user'),
]
