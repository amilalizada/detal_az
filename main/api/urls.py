from main.api.views import ContactAPIView
from django.urls import path



app_name = 'contactapi'
urlpatterns = [
    path('contact/',ContactAPIView.as_view(),name='contact'),
]