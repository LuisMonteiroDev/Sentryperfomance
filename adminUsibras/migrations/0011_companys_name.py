# Generated by Django 4.2.1 on 2023-06-11 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminUsibras', '0010_alter_companys_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='companys',
            name='name',
            field=models.CharField(default='', max_length=150, verbose_name='Nome da empresa'),
        ),
    ]
