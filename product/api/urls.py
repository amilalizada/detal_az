# from main.api.views import ContactAPIView, MainPageMarkaAPIView, WishlistAPIView , MainPageModelAPIView, FilteredProductAPIView
from django.urls import path
from product.api.views import *



app_name = 'productapi'
urlpatterns = [
    path('add-product/',CreatePoruct.as_view(),name='create-product'),
    path('category/',CategoryApiView.as_view(),name='category-api'),
    path('product-detail/<str:slug>', ProductDetail.as_view(), name='product-detail')
    # path('category-detail/',CategoryDetail.as_view(),name='category-detail-api'),
]