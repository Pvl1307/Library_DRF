from django.urls import path

from library.apps import LibraryConfig
from library.views import BookCreateListAPIView, BookRetrieveUpdateDestroyAPIView

app_name = LibraryConfig.name

urlpatterns = [
    path('books/', BookCreateListAPIView.as_view(), name='books_create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='books_create'),

    # path('books/create/', BookCreateAPIView.as_view(), name='books_create'),
    # path('books/', BookListAPIView.as_view(), name='books_list'),
    # path('books/<int:pk>/', BookRetrieveAPIView.as_view(), name='books_detail'),
    # path('books/update/<int:pk>/', BookUpdateAPIView.as_view(), name='books_update'),
    # path('books/delete/<int:pk>/', BookDestroyAPIView.as_view(), name='books_delete')
]
