# Generated by Django 3.2.7 on 2021-11-16 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='main_image',
        ),
    ]
