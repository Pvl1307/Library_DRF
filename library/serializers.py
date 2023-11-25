from rest_framework import serializers

from library.models import Book
from library.validators import validate_date, validate_isbn


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        validate_date(data.get('publication_year'))
        validate_isbn(data.get('isbn'))
        return data
