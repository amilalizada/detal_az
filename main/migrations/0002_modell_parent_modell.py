# Generated by Django 3.2.7 on 2021-10-11 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modell',
            name='parent_modell',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_models', to='main.modell', verbose_name='Parent Modell'),
        ),
    ]
