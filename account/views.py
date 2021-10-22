from django.db import models
from django.shortcuts import render, redirect
from django.urls import  reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from account.tasks import send_confirmation_mail
from account.forms import RegistrationForm,LoginForm
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView
)

User = get_user_model()

# class RegisterPageView(CreateView):
#     form_class = RegistrationForm
    
# def RegisterPageView(request):
#     form = RegistrationForm()
#     if request.method == 'POST':
#         form = RegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https
#             # send_confirmation_mail(user_id=user.id, site_address=site_address)
#             messages.success(request, 'Siz ugurla qeydiyyatdan kecdiniz')
#             return redirect(reverse_lazy('main:home'))
#     context = {
#         'form': form
#     }
#     return render(request, 'register.html', context)

class RegisterPageView(CreateView):
    form_class = RegistrationForm
    print("balam")
    success_url = reverse_lazy('account:login')
    template_name = 'register.html'

class LoginPageView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('main:home')


@login_required
def logout(request):
    django_logout(request)
    messages.success(request, 'Siz cixis etdiniz')
    return redirect(reverse_lazy('product:product_list'))


# class LoginPageView(TemplateView):
#     template_name = 'login.html'

# class RegisterPageView(TemplateView):
#     template_name = 'register.html'

class SelfProfilePageView(TemplateView):
    template_name = 'self-profile.html'

class UserProfilePageView(TemplateView):
    template_name = 'user-profile2.html'