from django.db import models
from django.shortcuts import render,redirect 

from django.views.generic import TemplateView



# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'
