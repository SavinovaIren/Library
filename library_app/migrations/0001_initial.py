# Generated by Django 4.1.6 on 2023-02-27 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя автора')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия автора')),
                ('photo', models.ImageField(upload_to='media/', verbose_name='Фото')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название книги')),
                ('description', models.TextField(verbose_name='Описание книги')),
                ('quantity_of_pages', models.IntegerField(verbose_name='Колличество страниц')),
                ('quantity_of_books', models.IntegerField(default=1, verbose_name='Колличество книг')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('author', models.ManyToManyField(blank=True, to='library_app.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя читателя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия читателя')),
                ('phone', models.BigIntegerField(verbose_name='Номер телефона')),
                ('status', models.CharField(choices=[('Active', 'Активный'), ('Inactive', 'Не активный')], default='Active', max_length=8, verbose_name='Статус читателя')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('active_books', models.ManyToManyField(blank=True, to='library_app.book', verbose_name='Активные книги')),
            ],
            options={
                'verbose_name': 'Читатель',
                'verbose_name_plural': 'Читатели',
                'ordering': ['first_name'],
            },
        ),
    ]
