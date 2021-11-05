from main.api.views import ContactAPIView, WhislistAPIView
from django.urls import path



app_name = 'contactapi'
urlpatterns = [
    path('contact/',ContactAPIView.as_view(),name='contact'),
    path('wishlist/',WhislistAPIView.as_view(),name='wishlist'),
]