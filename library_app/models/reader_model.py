from django.db import models


class Reader(models.Model):
    STATUS = [
        ("Active", "Активный"),
        ("Inactive", "Не активный"),
    ]
    first_name = models.CharField(verbose_name="Имя читателя", max_length=25)
    last_name = models.CharField(verbose_name="Фамилия читателя", max_length=50)
    phone = models.BigIntegerField(verbose_name="Номер телефона")
    status = models.CharField(max_length=8, choices=STATUS, verbose_name="Статус читателя", default="Inactive")
    active_books = models.ManyToManyField('Book', verbose_name="Активные книги", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def display_books(self):
        return ', '.join([book.name for book in self.active_books.all()])

    display_books.short_description = 'Активные книги'
