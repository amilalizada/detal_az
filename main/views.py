from django.db import models
from django.shortcuts import render,redirect 
from main.models import *
from django.views.generic import TemplateView
from django.views.generic import (
    ListView, DetailView
)


# Create your views here.
class HomePageView(ListView):
    model = Marka
    template_name = 'index.html'
    context_object_name = 'markalar'

    def get_markalar(self):
        markalar = Marka.objects.all().order_by('-created_at')[:8]
        return markalar


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['markalar'] = self.get_markalar()
        return context



class AboutPageView(TemplateView):
    template_name = 'about.html'


class AllBrandsView(ListView):
    template_name = 'all-brands.html'


class AllBrandsView(ListView):
    model = Marka
    template_name = 'all-brands.html'
    context_object_name = 'markalar'

    def get_markalar(self):
        markalar = Marka.objects.all().order_by('-created_at')
        return markalar


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['markalar'] = self.get_markalar()
        return context

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


