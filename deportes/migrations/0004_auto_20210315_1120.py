# Generated by Django 3.1.7 on 2021-03-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0003_auto_20210314_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='tipo',
        ),
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(default='', upload_to='albums/images/'),
        ),
        migrations.AlterField(
            model_name='deportes',
            name='imagen',
            field=models.ImageField(default='', upload_to='albums/images/'),
        ),
    ]