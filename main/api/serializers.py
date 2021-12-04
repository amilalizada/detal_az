from django.db import models
from django.db.models import fields
from rest_framework import permissions
from main.models import Contact, Marka, Modell, WishList
from product.models import Product
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'name',
            'phone_number',
        )


class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishList
        fields = (
            'user',
            'product',
        )
        

class MainPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marka
        fields = (
            'title',
            'id',
        )


class MainPageModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Modell
        fields = (
            'title',
            'id',
            'min_year',
            'max_year',
        )


class FilteredProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = (
            'title',
            'price',
            'description',
            'vin_code',
            'main_image',
            'discount',   
        )

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        permisson_classes = [permissions.IsAuthenticated]

        fields = (
            'id',
            'title',
            'price',
            'description',
            'vin_code',
            'main_image',
            'discount',   
            'is_active',
        )