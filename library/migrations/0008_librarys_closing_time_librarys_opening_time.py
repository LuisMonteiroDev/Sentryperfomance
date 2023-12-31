# Generated by Django 4.2.2 on 2023-12-01 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_librarys_books_for_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarys',
            name='closing_time',
            field=models.TimeField(default='21:00', verbose_name='Horário de fechamento'),
        ),
        migrations.AddField(
            model_name='librarys',
            name='opening_time',
            field=models.TimeField(default='08:00', verbose_name='Horário de abertura'),
        ),
    ]
