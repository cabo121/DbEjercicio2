# Generated by Django 3.1.7 on 2021-03-14 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(default='')),
                ('descripcion', models.TextField(default='')),
                ('tipo', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.TextField(default='')),
                ('comentario', models.TextField(default='')),
                ('fecha', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='deportes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.TextField(default='')),
                ('deporte', models.TextField(default='')),
                ('fecha', models.TextField(default='')),
            ],
        ),
    ]
