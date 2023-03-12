from django.contrib.auth.models import AbstractUser
from django.db import models


class Reader(AbstractUser):
    phone = models.BigIntegerField(verbose_name="Номер телефона")
    active_books = models.ManyToManyField('Book', verbose_name="Активные книги", blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    is_active = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='myuser_set',
        blank=True,
        help_text='Группы, к которым принадлежит этот пользователь. Пользователь получит все разрешения, предоставленные каждой из своих групп.',
        verbose_name='Группы',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='myuser_set',
        blank=True,
        help_text='Особые разрешения для этого пользователя.',
        verbose_name='Разрешения пользователя',
    )

    class Meta:
        app_label = 'library_app'
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"
        ordering = ['first_name']

    def __str__(self):
        return f"{self.username}"

    def display_books(self):
        return ', '.join([book.name for book in self.active_books.all()])

    display_books.short_description = 'Активные книги'


class Author(models.Model):
    first_name = models.CharField(verbose_name="Имя автора", max_length=25)
    last_name = models.CharField(verbose_name="Фамилия автора", max_length=50)
    photo = models.ImageField(upload_to="media/", verbose_name="Фото")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    name = models.CharField(verbose_name="Название книги", max_length=50)
    description = models.TextField(verbose_name="Описание книги")
    quantity_of_pages = models.IntegerField(verbose_name="Колличество страниц")
    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.PROTECT)
    quantity_of_books = models.PositiveIntegerField(verbose_name="Колличество книг", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"
