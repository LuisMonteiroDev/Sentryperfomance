# Generated by Django 4.2.2 on 2023-12-21 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0011_librarys_type_payments_accepted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adverts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.ImageField(upload_to='', verbose_name='Anúncio')),
                ('create_at', models.DateTimeField(verbose_name='Data de início')),
                ('expiration', models.DateTimeField(verbose_name='Data de expiração')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='library_adverts', to='library.librarys', verbose_name='Biblioteca anunciante')),
            ],
            options={
                'verbose_name': 'Anúncio',
                'verbose_name_plural': 'Anúncios',
            },
        ),
    ]
