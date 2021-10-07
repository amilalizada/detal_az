from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [
    path('/',ProductPageView.as_view(),name='products'),
    path('/add-product',AddProductPageView.as_view(),name='add-product'),
    path('/sale-products',SaleProductPageView.as_view(),name='sale-products'),
]