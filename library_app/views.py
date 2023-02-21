from django.shortcuts import render
from rest_framework.generics import ListAPIView

from library_app.models import Book, Reader, Author
from library_app.serializers import ReaderSerializer, BookSerializer, AuthorSerializer


class ReaderView(ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class BookView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
