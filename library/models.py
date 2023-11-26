from django.db import models


class Book(models.Model):
    """Модель книги"""
    title = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.CharField(max_length=100, verbose_name='Автор')
    publication_year = models.IntegerField(verbose_name='Год публикации')
    isbn = models.CharField(max_length=17, unique=True, verbose_name='ISBN')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
