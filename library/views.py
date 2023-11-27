from rest_framework import generics

from library.models import Book
from library.paginators import BookPaginator
from library.serializers import BookSerializer


class BookCreateListAPIView(generics.ListCreateAPIView):
    """Создание и список книг"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    pagination_class = BookPaginator

    def perform_create(self, serializer):
        """Сохранение созданной книги"""
        serializer.save()


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Обновление, удаление и просмотр выбранной книги"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
