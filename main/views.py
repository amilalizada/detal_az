from django.db import models
from django.shortcuts import render,redirect 

from django.views.generic import TemplateView



# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class AllBrandsView(TemplateView):
    template_name = 'all-brands.html'


class AllBrandsView(TemplateView):
    template_name = 'all-brands.html'


class BrandsView(TemplateView):
    template_name = 'brands.html'


class CarDetailView(TemplateView):
    template_name = 'car_detail.html'


class CarFilterView(TemplateView):
    template_name = 'car-filter.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class InnerDetailView(TemplateView):
    template_name = 'inner-details.html'


class ShopsView(TemplateView):
    template_name = 'shops.html'


class SinglePageView(TemplateView):
    template_name = 'singlepage.html'


class WishlistPageView(TemplateView):
    template_name = 'wishlist.html'


