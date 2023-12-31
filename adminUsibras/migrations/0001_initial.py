# Generated by Django 4.2.1 on 2023-05-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Titulo')),
                ('release_year', models.IntegerField(verbose_name='Ano de lançamento')),
                ('state', models.CharField(max_length=50, verbose_name='Estado')),
                ('pages', models.IntegerField(verbose_name='Quantidade de páginas')),
                ('publishing_company', models.CharField(max_length=255, verbose_name='Publicado pela empresa')),
                ('create_at', models.DateField(verbose_name='Data de criação')),
                ('image', models.ImageField(upload_to='', verbose_name='Foto do livro')),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
            },
        ),
    ]
