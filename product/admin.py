from django.contrib import admin
from main.models import *
from product.models import Category, Product

# admin.site.register(Tours)
admin.site.register(Category)
admin.site.register(Product)