from main.api.serializers import ContactSerializer , WishListSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from main.models import Contact, WishList


class ContactAPIView(CreateAPIView):
    serializer_class = ContactSerializer
    model = Contact


class WhislistAPIView(CreateAPIView):
    serializer_class = WishListSerializer
    model = WishList

     