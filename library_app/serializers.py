from rest_framework.serializers import ModelSerializer

from library_app.models import Reader, Author, Book


class ReaderSerializer(ModelSerializer):
    class Meta:
        model = Reader
        fields = "__all__"


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"



class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"