from django.db import models
from django.db.models import fields
from main.models import Contact, WishList
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
        