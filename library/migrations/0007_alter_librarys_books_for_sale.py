# Generated by Django 4.2.2 on 2023-11-06 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminUsibras', '0015_books_price'),
        ('library', '0006_librarys_books_for_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarys',
            name='books_for_sale',
            field=models.ManyToManyField(limit_choices_to={'in_stock': True}, related_name='library_books_for_sale', to='adminUsibras.books', verbose_name='Livros à venda'),
        ),
    ]
