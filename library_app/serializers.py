from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from library_app.models import Reader, Author, Book
import re


class PhoneValidator:
    def __call__(self, value):
        phone = re.compile(r"^[7](\d{10})$")
        if not phone.search(str(value)):
            raise serializers.ValidationError("Введите номер в формате 7**********")
        else:
            return value


class CountValidator:
    def __call__(self, value):
        if value < 0:
            raise serializers.ValidationError("Колличество не может быть отрицательным")

class ActiveBookCount:
    def __call__(self, value):
        if value > 3:
            raise serializers.ValidationError('Нельзя добавить больше 3 книг')


class BookValidator:

    def update(self, instance, validated_data):
        if validated_data['book']:
            # Уменьшаем количество экземпляров книги, если книга добавляется в актив читателя
            for book in validated_data['book']:
                if book not in instance.book.all():
                    if book.quantity > 0:
                        book.quantity -= 1
                        book.save()
                    else:
                        raise serializers.ValidationError(f'Книга {book.title} отсутствует')
            # Увеличиваем количество экземпляров книги, если книга удаляется из актива читателя
            for book in instance.book.all():
                if book not in validated_data['book']:
                    book.quantity += 1
                    book.save()

        return super().update(instance, validated_data)


class ReaderSerializer(ModelSerializer):
    active_books = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='name', many=True,
                                                validators=[ActiveBookCount()])
    phone = serializers.IntegerField(validators=[PhoneValidator()])


    class Meta:
        model = Reader
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='last_name')
    quantity_of_pages = serializers.IntegerField(validators=[CountValidator()])
    quantity_of_books = serializers.IntegerField(validators=[BookValidator()])

    quantity_of_books.short_description = "Колличество книг в библиотеке"

    class Meta:
        model = Book
        fields = '__all__'
