# Generated by Django 4.1.6 on 2023-03-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_alter_reader_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='quantity_of_books',
            field=models.PositiveIntegerField(default=1, verbose_name='Колличество книг'),
        ),
    ]
