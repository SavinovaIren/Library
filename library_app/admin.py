from django.contrib import admin

from library_app.models import Author, Book, Reader

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Reader)