from rest_framework import generics

from users.serializers import UserSerializer
from users.tasks import send_registration_mail


class RegisterUserAPIView(generics.CreateAPIView):
    """Регистрация пользователя"""
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Сохранение созданного пользователя"""
        user = serializer.save()
        send_registration_mail.delay(user.email)
