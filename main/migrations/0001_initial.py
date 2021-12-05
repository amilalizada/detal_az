# Generated by Django 3.2.7 on 2021-12-05 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('phone_number', models.PositiveIntegerField(verbose_name='Phone Number')),
            ],
            options={
                'verbose_name': 'Our Contact',
                'verbose_name_plural': 'Our Contacts',
            },
        ),
        migrations.CreateModel(
            name='Marka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Basligi')),
                ('title_en', models.CharField(max_length=120, null=True, verbose_name='Basligi')),
                ('title_az', models.CharField(max_length=120, null=True, verbose_name='Basligi')),
                ('title_ru', models.CharField(max_length=120, null=True, verbose_name='Basligi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='marka_image', verbose_name='Image')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Marka',
                'verbose_name_plural': 'Markalar',
            },
        ),
        migrations.CreateModel(
            name='Modell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Basligi')),
                ('title_en', models.CharField(max_length=120, null=True, verbose_name='Basligi')),
                ('title_az', models.CharField(max_length=120, null=True, verbose_name='Basligi')),
                ('title_ru', models.CharField(max_length=120, null=True, verbose_name='Basligi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='model_image', verbose_name='Image')),
                ('is_parent', models.BooleanField(default=False, verbose_name='esas model')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Modeller',
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Arzu Listi',
                'verbose_name_plural': 'Arzu Listleri',
            },
        ),
    ]
