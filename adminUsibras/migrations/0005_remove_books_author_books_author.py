# Generated by Django 4.2.1 on 2023-06-10 17:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminUsibras', '0004_alter_books_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='author',
        ),
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.ManyToManyField(default='', to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]
