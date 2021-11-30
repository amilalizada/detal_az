from django.db import models
from django.db.models import fields
from main.models import Contact, Marka, Modell, WishList
from product.models import Product
from account.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )


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
    user_id = UserSerializer()

    class Meta:
        model = Product

        fields = (
            'id',
            'user_id',
            'title',
            'price',
            'description',
            'vin_code',
            'main_image',
            'discount',
        )