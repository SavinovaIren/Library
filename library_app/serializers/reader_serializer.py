from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
import re

from library_app.models.book_model import Book

from library_app.models.reader_model import Reader


class PhoneValidator:
    def __call__(self, value):
        phone = re.compile(r"^[7](\d{10})$")
        if not phone.search(str(value)):
            raise serializers.ValidationError("Введите номер в формате 7**********")
        else:
            return value


class ReaderSerializer(ModelSerializer):
    active_books = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='name', many=True)
    phone = serializers.IntegerField(validators=[PhoneValidator()])

    def validate(self, attrs):
        if len(attrs['active_books']) > 3:
            raise serializers.ValidationError('Нельзя добавить больше 3 книг')
        return attrs

    def update(self, instance, validated_data):
        if validated_data['active_books']:
            # Уменьшаем количество экземпляров книги, если книга добавляется в актив читателя
            for book in validated_data['active_books']:
                if book not in instance.book.all():
                    if book.quantity > 0:
                        book.quantity -= 1
                        book.save()
                    else:
                        raise ValidationError(f'Книга {book.title} отсутствует')
            # Увеличиваем количество экземпляров книги, если книга удаляется из актива читателя
            for book in instance.book.all():
                if book not in validated_data['active_books']:
                    book.quantity += 1
                    book.save()

        return super().update(instance, validated_data)

    class Meta:
        model = Reader
        fields = '__all__'
