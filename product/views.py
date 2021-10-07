from django.db import models
from django.shortcuts import render,redirect 

from django.views.generic import TemplateView



# Create your views here.
class AddProductPageView(TemplateView):
    template_name = 'add-product.html'


class ProductPageView(TemplateView):
    template_name = 'products.html'

class SaleProductPageView(TemplateView):
    template_name = 'sale-products.html'