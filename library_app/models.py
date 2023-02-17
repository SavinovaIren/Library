from django.db import models


class Reader(models.Model):
    STATUS = [
        ("Active", "Активный"),
        ("Inactive", "Не активный"),
    ]
    first_name = models.CharField(verbose_name="Имя читателя", max_length=25)
    last_name = models.CharField(verbose_name="Фамилия читателя", max_length=50)
    status = models.CharField(max_length=8, choices=STATUS, verbose_name="Статус читателя", default="Active")
    active_books = models.ManyToManyField('Book', verbose_name="Активные книги", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    name = models.CharField(verbose_name="Название книги", max_length=50)
    description = models.TextField(verbose_name="Описание книги")
    quantity_of_pages = models.IntegerField(verbose_name="Колличество страниц")
    author = models.ManyToManyField('Author', verbose_name="Автор", blank=True)
    quantity_of_books = models.IntegerField(verbose_name="Колличество книг")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['name']

    def __str__(self):
        return f"{self.author} {self.name}"



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