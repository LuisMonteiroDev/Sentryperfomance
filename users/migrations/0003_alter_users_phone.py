# Generated by Django 4.2.2 on 2023-07-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_company_owner_users_library_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Telefone'),
        ),
    ]
