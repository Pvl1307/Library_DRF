from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
