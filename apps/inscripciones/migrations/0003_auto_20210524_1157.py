# Generated by Django 2.2.4 on 2021-05-24 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0002_auto_20210523_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='confirmado',
            field=models.BooleanField(default=1),
        ),
    ]
