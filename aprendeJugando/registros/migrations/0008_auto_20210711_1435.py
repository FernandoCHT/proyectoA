# Generated by Django 3.2.4 on 2021-07-11 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0007_auto_20210711_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Actualizado'),
        ),
    ]
