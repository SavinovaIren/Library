from django.contrib import admin

from django.db.models import QuerySet
from django.utils.html import format_html
from django.urls import reverse

from library_app.models.author_model import Author
from library_app.models.book_model import Book
from library_app.models.reader_model import Reader


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity_of_pages', 'author_link', 'quantity_of_books', 'created', 'updated')
    actions = ['set_null_quantity']

    def author_link(self, obj):
        author = obj.author
        url = reverse("admin:library_app_author_changelist") + str(author.pk)
        return format_html(f'<a href="{url}"> {author} </a>')

    author_link.short_description = "Автор"

    @admin.action(description='Установить колличество 0')
    def set_null_quantity(self, request, queryset):
        queryset.update(quantity_of_books=0)


class ReaderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'status', 'display_books', 'created', 'updated')
    list_filter = ('status',)
    actions = ['change_status', 'books_delete', 'cancel_book_selected']

    @admin.action(description='Изменить статус пользователя')
    def change_status(self, request, queryset: QuerySet):
        queryset.update(status='Inactive')

    @admin.action(description='Удалить книги из актива читателя')
    def cancel_book_selected(self, request, queryset):

        for reader in queryset.all():
            for active_books in reader.active_books.all():
                active_books = Book.objects.get(pk=active_books.pk)
                active_books.quantity_of_books += 1
                active_books.save()
                reader.active_books.remove(active_books)






class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created', 'updated')


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Reader, ReaderAdmin)