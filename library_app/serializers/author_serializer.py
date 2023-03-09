from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from library_app.models.author_model import Author


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
