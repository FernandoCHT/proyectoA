# Generated by Django 3.2.4 on 2021-08-25 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0015_administrador_comentariocliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='fotos', verbose_name='Fotografía'),
        ),
    ]
