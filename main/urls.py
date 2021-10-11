from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('/',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('allbrands/',AllBrandsView.as_view(),name='allbrands'),
    path('brands/',BrandsView.as_view(),name='brands'),
    path('car-filter/',CarFilterView.as_view(),name='car-filter'),
    path('car-detail/',CarDetailView.as_view(),name='car-detail'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('shops/',ShopsView.as_view(),name='contact'),
    path('inner-details/',InnerDetailView.as_view(),name='inner-details'),
    path('single-page/',SinglePageView.as_view(),name='isingle-page'),
    path('wishlist/',WishlistPageView.as_view(),name='wishlist'),

    
    
]