from main.api.serializers import ContactSerializer
from rest_framework.generics import CreateAPIView
from main.models import Contact


class ContactAPIView(CreateAPIView):
    serializer_class = ContactSerializer
    model = Contact