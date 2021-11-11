from django.contrib.auth.models import AnonymousUser
from django.db import models
from django.http import request
from django.shortcuts import render,redirect
from main.models import WishList 
from product.models import Product
from django.views.generic import TemplateView
from django.views.generic import (
    ListView, DetailView
)


# Create your views here.
class AddProductPageView(TemplateView):
    template_name = 'add-product.html'


class ProductPageView(TemplateView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'sale-products'

    def get_products(self):
        sale_products = Product.objects.all().order_by('-created_at')
        return sale_products


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.get_products()
        if self.request.user.is_authenticated: 
            print('wawawawawawaawaw')
            wishlists = WishList.objects.filter(user= self.request.user)
            print(wishlists)
            wish_products = []
            for i in wishlists:
                title = i.product.title
                wish_products.append(title)
            # print(wish_products)
            context['wishes'] = wish_products
        return context


class SaleProductPageView(ListView):
    model = Product
    template_name = 'sale-products.html'
    context_object_name = 'sale-products'

    def get_sale_products(self):
        sale_products = Product.objects.filter(is_discount = True)
        return sale_products


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sale'] = self.get_sale_products()
        return context