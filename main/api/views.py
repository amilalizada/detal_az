from main.api.serializers import ContactSerializer , WishListSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from main.models import Contact, WishList
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class ContactAPIView(CreateAPIView):
    serializer_class = ContactSerializer
    model = Contact


class WishlistAPIView(APIView):


    def get(self, request, format=None):
        snippets = WishList.objects.all()
        serializer = WishListSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WishListSerializer(data=request.data)
        if serializer.is_valid():
            print('in post')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        product_id = request.data.get('product')
        print('1----', self)
        obj = WishList.objects.filter(product = product_id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



     