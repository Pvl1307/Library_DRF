from rest_framework import generics

from library.models import Book
from library.paginators import BookPaginator
from library.serializers import BookSerializer


class BookCreateAPIView(generics.CreateAPIView):
    """Создание книги"""
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        """Сохранение созданной книги"""
        serializer.save()


class BookListAPIView(generics.ListAPIView):
    """Список книг"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    pagination_class = BookPaginator


class BookRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр выбранной книги"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookUpdateAPIView(generics.RetrieveUpdateAPIView):
    """Обновление книги"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def perform_update(self, serializer):
        """Сохранение обновления книги"""
        serializer.save()


class BookDestroyAPIView(generics.DestroyAPIView):
    """Удаление выбранной книги"""
    queryset = Book.objects.all()
