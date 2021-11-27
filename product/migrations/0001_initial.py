# Generated by Django 3.2.7 on 2021-11-26 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
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
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('vin_code', models.CharField(blank=True, max_length=120, null=True, verbose_name='Vin code')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Qiymet')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='Discount Percentage')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='product_image', verbose_name='Main Image')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_image', verbose_name='Image')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='slug')),
                ('is_discount', models.BooleanField(default=False, verbose_name='Is Discount')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='product.category', verbose_name='Category')),
                ('marka_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marka_product', to='main.marka', verbose_name='Marka')),
                ('modell_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_product', to='main.modell', verbose_name='Modell')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_product', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
