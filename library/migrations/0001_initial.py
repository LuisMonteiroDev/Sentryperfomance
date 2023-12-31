# Generated by Django 4.2.2 on 2023-07-02 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminUsibras', '0013_companys_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Librarys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome da livraria')),
                ('address', models.CharField(max_length=50, verbose_name='Endereço')),
                ('partner_companies', models.ManyToManyField(related_name='library_partner_companies', to='adminUsibras.companys', verbose_name='Companhias parceiras')),
            ],
            options={
                'verbose_name': 'Biblioteca',
                'verbose_name_plural': 'Bibliotecas',
            },
        ),
    ]
