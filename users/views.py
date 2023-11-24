from rest_framework import generics

from users.serializers import UserSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    """Регистрация пользователя"""
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Сохранение созданного пользователя"""
        serializer.save()
