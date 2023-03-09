from rest_framework.viewsets import ModelViewSet

from library_app.models.author_model import Author
from library_app.models.book_model import Book
from library_app.models.reader_model import Reader
from library_app.serializers.author_serializer import AuthorSerializer
from library_app.serializers.book_serializer import BookSerializer

from library_app.serializers.reader_serializer import ReaderSerializer


class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
