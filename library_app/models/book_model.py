from django.db import models

from .author_model import Author


class Book(models.Model):
    name = models.CharField(verbose_name="Название книги", max_length=50)
    description = models.TextField(verbose_name="Описание книги")
    quantity_of_pages = models.IntegerField(verbose_name="Колличество страниц")
    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.PROTECT)
    quantity_of_books = models.IntegerField(verbose_name="Колличество книг", default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"
