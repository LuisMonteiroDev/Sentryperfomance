# Generated by Django 4.2.2 on 2023-12-13 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_methods', '0001_initial'),
        ('library', '0010_alter_librarys_maximum_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarys',
            name='type_payments_accepted',
            field=models.ManyToManyField(related_name='type_payments_accepted', to='payment_methods.paymentmethods', verbose_name='Tipos de pagamentos aceitos'),
        ),
    ]
