from django.contrib import admin

from library_app.models import Author, Book, Reader
from django.db.models import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity_of_pages', 'author_link', 'quantity_of_books', 'created', 'updated')

    def author_link(self, obj):
        author = obj.author
        url = reverse("admin:library_app_author_changelist") + str(author.pk)
        return format_html(f'<a href="{url}"> {author} </a>')

    author_link.short_description = "Автор"


class ReaderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'status', 'display_books', 'created', 'updated')
    list_filter = ('status',)
    actions = ['change_status', 'books_delete']

    @admin.action(description='Изменить статус пользователя')
    def change_status(self, request, queryset: QuerySet):
        queryset.update(status='Inactive')


    @admin.action(description='Удалить все книги пользователя')
    def books_delete(self, request, queryset: QuerySet):
        books = Reader.objects.get(active_books=request)
        books.active_books.remove()


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created', 'updated')


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Reader, ReaderAdmin)