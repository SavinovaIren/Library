from django.db import models


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
