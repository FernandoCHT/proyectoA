# Generated by Django 3.2.4 on 2021-08-24 20:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0012_auto_20210824_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Actualizado'),
            preserve_default=False,
        ),
    ]
