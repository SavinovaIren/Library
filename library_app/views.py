from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from library_app.models import Author, Book
from library_app.permissions import PermissionPolicyMixin, IsAdminOrOwner

Reader = get_user_model()
from library_app.serializers.author_serializer import AuthorSerializer
from library_app.serializers.book_serializer import BookSerializer
from library_app.serializers.reader_serializer import ReaderSerializer


class ReaderViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes_per_method = {
        "list": [IsAdminOrOwner],
        "create": [AllowAny],
        "update": [IsAdminOrOwner],
        "destroy": [IsAdminOrOwner]
    }

class BookViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes_per_method = {
        "list": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }


class AuthorViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes_per_method = {
        "list": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
