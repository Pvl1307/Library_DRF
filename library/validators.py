from rest_framework.serializers import ValidationError


def validate_date(date):
    """Валидация даты, проверяет, что дата должна быть больше 1000 года."""
    if date < 1000:
        raise ValidationError('Дата должна быть больше 1000 года')


def validate_isbn(isbn):
    """Валидация ISBN, проверяет, что ISBN содержит корректные символы."""
    parts = isbn.split('-')

    # Проверка количества частей и их содержимого
    if len(parts) != 5 or not all(part.isdigit() for part in parts):
        raise ValidationError('ISBN должен быть в формате XXX-X-XXXXX-XXX-X, где X - цифры.')
