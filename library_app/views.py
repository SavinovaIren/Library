from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from library_app.models import Book, Reader, Author
from library_app.serializers import ReaderSerializer, BookSerializer, AuthorSerializer


class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
