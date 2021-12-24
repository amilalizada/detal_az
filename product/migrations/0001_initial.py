# Generated by Django 3.2.7 on 2021-12-24 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_auto_20211224_0852'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True, verbose_name='Title')),
                ('title_en', models.CharField(blank=True, max_length=120, null=True, verbose_name='Title')),
                ('title_az', models.CharField(blank=True, max_length=120, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(blank=True, max_length=120, null=True, verbose_name='Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_image', verbose_name='Image')),
                ('category_order', models.IntegerField(blank=True, null=True, verbose_name='Category Order')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='slug')),
                ('is_parent', models.BooleanField(default=False, verbose_name='Is Parent')),
                ('is_box_category', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Box Category')),
                ('is_long_box_category', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Long Box Category')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='product.category', verbose_name='Parent Category')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('title_en', models.CharField(max_length=120, null=True, verbose_name='Title')),
                ('title_az', models.CharField(max_length=120, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=120, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_az', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('vin_code', models.CharField(blank=True, max_length=120, null=True, verbose_name='Vin code')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Qiymet')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='Discount Percentage')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='product_image', verbose_name='Main Image')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='slug')),
                ('is_discount', models.BooleanField(default=False, verbose_name='Is Discount')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is_active')),
                ('is_vip', models.BooleanField(default=False, verbose_name='Is Vip')),
                ('is_new', models.BooleanField(default=False, verbose_name='Is New')),
                ('watch_count', models.IntegerField(default=0, verbose_name='Watch Count')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='product.category', verbose_name='Category')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_city', to='product.city', verbose_name='City')),
                ('marka_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marka_product', to='main.marka', verbose_name='Marka')),
                ('modell_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_product', to='main.modell', verbose_name='Modell')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_product', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_image', verbose_name='Image')),
                ('is_main', models.BooleanField(default=False, verbose_name='Is Main')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
