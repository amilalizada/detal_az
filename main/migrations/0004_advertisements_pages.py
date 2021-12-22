# Generated by Django 3.2.7 on 2021-12-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_advertisements'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements',
            name='pages',
            field=models.CharField(blank=True, choices=[('Main Page', 'Əsas Səhife'), ('About Page', 'Haqqimizda'), ('All Brands Page', 'Butun Markalar'), ('All Models Page', 'Butun Modeller'), ('Car Detail Page', 'Esas Kateqoriyalar')], max_length=50, null=True, verbose_name='Sehifeler'),
        ),
    ]