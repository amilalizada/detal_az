# Generated by Django 3.2.7 on 2021-12-23 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211223_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title_az',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title_en',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title_ru',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Qiymet'),
        ),
    ]
