from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from library_app.models.author_model import Author

from library_app.models.book_model import Book

class CountValidator:
    def __call__(self, value):
        if value < 0:
            raise serializers.ValidationError("Колличество не может быть отрицательным")

class BookSerializer(ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='last_name')
    quantity_of_pages = serializers.IntegerField(validators=[CountValidator()])
    quantity_of_books = serializers.IntegerField()

    quantity_of_books.short_description = "Колличество книг в библиотеке"

    class Meta:
        model = Book
        fields = '__all__'
