# Generated by Django 4.2.2 on 2023-11-13 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminUsibras', '0017_companys_email_companys_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companys',
            name='cnpj',
            field=models.CharField(max_length=14, unique=True, verbose_name='CNPJ'),
        ),
    ]
