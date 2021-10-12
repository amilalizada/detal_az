from django.db import models
from django.shortcuts import render,redirect 
from main.models import *
from django.views.generic import TemplateView
from django.views.generic import (
    ListView, DetailView
)
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


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

class BrandsView(DetailView):
    model = Marka
    template_name = 'brands.html'
    context_object_name = 'marka'

    def get_success_url(self , **kwargs):
        return reverse_lazy('main:brands' , kwargs = {'pk': self.object.pk})

    def get_modeller(self):
        print(self.object.id,'buradi')
        modeller = Modell.objects.filter(marka_id=self.object.pk)
        return modeller


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modeller'] = self.get_modeller()
        return context


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


