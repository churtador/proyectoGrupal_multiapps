# Generated by Django 2.2.4 on 2021-05-21 23:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
                ('apellido', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
                ('fecha_Nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('acceso', models.CharField(choices=[('0', 'alumno'), ('1', 'profesor')], default=0, max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
