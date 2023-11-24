from django.urls import path

from library.apps import LibraryConfig
from library.views import BookCreateAPIView, BookListAPIView, BookRetrieveAPIView, BookUpdateAPIView, BookDestroyAPIView

app_name = LibraryConfig.name

urlpatterns = [
    path('books/create/', BookCreateAPIView.as_view(), name='books_create'),
    path('books/', BookListAPIView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookRetrieveAPIView.as_view(), name='books_detail'),
    path('books/update/<int:pk>/', BookUpdateAPIView.as_view(), name='books_update'),
    path('books/delete/<int:pk>/', BookDestroyAPIView.as_view(), name='books_delete')
]
