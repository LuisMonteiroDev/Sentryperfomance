# Generated by Django 4.2.2 on 2023-12-16 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_users_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='type_user',
            field=models.CharField(choices=[('default', 'Padrão'), ('owner', 'Dono')], default='default', max_length=100, verbose_name='Tipo do usuário'),
        ),
    ]
