from main.api.views import ContactAPIView, WishlistAPIView
from django.urls import path



app_name = 'contactapi'
urlpatterns = [
    path('contact/',ContactAPIView.as_view(),name='contact'),
    path('wishlist/',WishlistAPIView.as_view(),name='wishlist'),
]