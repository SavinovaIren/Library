from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from library_app.models import Reader, Author, Book


class ReaderSerializer(ModelSerializer):
    active_books = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='name', many=True)
    class Meta:
        model = Reader
        fields = "__all__"


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"



class BookSerializer(ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='last_name', many=True)
    class Meta:
        model = Book
        fields = "__all__"