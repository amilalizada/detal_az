# Generated by Django 3.2.7 on 2021-12-21 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_advertisements_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='pages',
            field=models.CharField(blank=True, choices=[('Main Page', 'Əsas Səhife'), ('About Page', 'Haqqimizda'), ('All Brands Page', 'Butun Markalar'), ('All Models Page', 'Butun Modeller'), ('Car Detail Page', 'Esas Kateqoriyalar'), ('Car Filter Page', 'Orta Kateqoriyalar'), ('Contact Page', 'Kontakt Sehifesi'), ('Inner Details Page', 'Ic Detallar'), ('Searched Products', 'Axtarilan Detallar'), ('Shops Page', 'Maqazinler'), ('Sub Parts Page', 'Ic Kateqoriyalar'), ('Wish List Page', 'Arzu Listi Sehifesi'), ('Change Password Page', 'Sifreni Deyisme Sehifesi'), ('Forget Password Page', 'Sifreni Unutdum Sehifesi'), ('Login Page', 'Hesaba Daxil Olmaq'), ('Reset Password Page', 'Sifreni Yenilemek'), ('Register Page', 'Registrasiyadan Kecmek'), ('Self Profile', 'Profil Sehifesi'), ('User Profile', 'Basqa Userin Profili'), ('Add Product', 'Product Elave Etmek'), ('Filtered Product', 'Filtrlenmis Detallar'), ('Products Page', 'Productlar Sehifesi'), ('Sale Product', 'Endirimde Olan Mehsullar'), ('Single Produt', 'Productun Sehifesi'), ('Update Product', 'Productun Duzelis Sehifesi')], max_length=50, null=True, verbose_name='Sehifeler'),
        ),
    ]
