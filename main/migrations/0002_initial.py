# Generated by Django 3.2.7 on 2021-12-05 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wish_user_product', to='product.product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wish_user', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='modell',
            name='marka_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marka_model', to='main.marka', verbose_name='Marka'),
        ),
        migrations.AddField(
            model_name='modell',
            name='parent_modell',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_models', to='main.modell', verbose_name='Parent Modell'),
        ),
    ]
