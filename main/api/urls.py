from main.api.views import ContactAPIView, MainPageMarkaAPIView, WishlistAPIView , MainPageModelAPIView, FilteredProductAPIView
from django.urls import path



app_name = 'contactapi'
urlpatterns = [
    path('contact/',ContactAPIView.as_view(),name='contact'),
    path('wishlist/',WishlistAPIView.as_view(),name='wishlist'),
    path('main/',MainPageMarkaAPIView.as_view(),name='main'),
    path('main-model/',MainPageModelAPIView.as_view(),name='main-model'),
    path('filtered-prod/',FilteredProductAPIView.as_view(),name='filtered-prod'),
]