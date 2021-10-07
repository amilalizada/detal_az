from django.db import models
from django.shortcuts import render,redirect 

from django.views.generic import TemplateView


class LoginPageView(TemplateView):
    template_name = 'login.html'

class RegisterPageView(TemplateView):
    template_name = 'register.html'

class SelfProfilePageView(TemplateView):
    template_name = 'self-profile.html'

class UserProfilePageView(TemplateView):
    template_name = 'user-profile2.html'