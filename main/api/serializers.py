from django.db.models import fields
from main.models import Contact
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'name',
            'phone_number',
        )