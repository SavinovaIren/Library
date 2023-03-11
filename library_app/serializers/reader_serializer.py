from rest_framework import serializers
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
        books = attrs.get('active_books', [])
        for book in books:
            if book.quantity_of_books == 0:
                raise serializers.ValidationError(f'Книги {book.name} нет в наличии')

        if len(books) > 3:
            raise serializers.ValidationError('Нельзя добавить больше 3 книг')
        return attrs



    def create(self, validated_data):
        active_books = validated_data.pop('active_books', [])
        reader = super().create(validated_data)
        for book in active_books:
            book.quantity_of_books -= 1
            book.save()
            reader.active_books.add(book)
        return reader

    def update(self, instance, validated_data):
        books = validated_data.pop('active_books', [])
        reader = super().update(instance, validated_data)

        #Получение книг
        new_list_books = set(books)
        old_list_books = set(instance.active_books.all())

        #Обновление количества книг
        for book in old_list_books - new_list_books:
            book.quantity_of_books += 1
            book.save()

        for book in new_list_books - old_list_books:
            book.quantity_of_books -= 1
            book.save()

        #Добавление книги
        for book in new_list_books - old_list_books:
            instance.active_books.add(book)

        #Удаление книги
        for book in old_list_books - new_list_books:
            instance.active_books.remove(book)

        return reader

    class Meta:
        model = Reader
        fields = '__all__'
