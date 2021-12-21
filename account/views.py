from django.db import models
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, \
    PasswordResetConfirmView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView
from account.tasks import send_confirmation_mail
from account.forms import EditProfileForm, RegistrationForm, LoginForm, CustomPasswordChangeForm, CustomPasswordResetForm, ResetPasswordForm
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from product.models import Product
from main.models import *

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
#             # send_confirmation_mail(user_id=user.id, _address=site_address)
#             messages.success(request, 'Siz ugurla qeydiyyatdan kecdiniz')
#             return redirect(reverse_lazy('main:home'))
#     context = {
#         'form': form
#     }
#     return render(request, 'register.html', context)


class RegisterPageView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('account:login')
    template_name = 'register.html'

    def form_valid(self, form):
        print(form.data, 'form')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reklamlar = Advertisements.objects.filter(pages ='Register Page')
        context['reklamlar'] = reklamlar
        return context


class LoginPageView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('main:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reklamlar = Advertisements.objects.filter(pages ='Login Page')
        context['reklamlar'] = reklamlar
        return context


# class ResetPasswordPageView(TemplateView):
#     template_name= 'reset_password.html'

class ChangePasswordPageView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        messages.success(self.request, 'Password set olundu')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reklamlar = Advertisements.objects.filter(pages ='Change Password Page')
        context['reklamlar'] = reklamlar
        return context


class ForgetPasswordView(PasswordResetView):
    email_template_name = 'email/password_reset_email.html'
    template_name = 'forget_password.html'
    success_url = reverse_lazy('account:login')
    form_class = CustomPasswordResetForm

    def form_valid(self, form):
        messages.success(
            self.request, 'password deyisilmesi ucun sizin mail-e mesaj gonderildi!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reklamlar = Advertisements.objects.filter(pages ='Forget Password Page')
        context['reklamlar'] = reklamlar
        return context


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset_password.html'
    success_url = reverse_lazy('account:login')
    form_class = ResetPasswordForm

    def form_valid(self, form):
        messages.success(self.request, 'password deyisdirildi')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reklamlar = Advertisements.objects.filter(pages ='Reset Password Page')
        context['reklamlar'] = reklamlar
        return context


# @login_required
# def logout(request):
#     django_logout(request)
#     messages.success(request, 'Siz cixis etdiniz')
#     return redirect(reverse_lazy('product:product_list'))


# class LoginPageView(TemplateView):
#     template_name = 'login.html'

# class RegisterPageView(TemplateView):
#     template_name = 'register.html'

class SelfProfilePageView(LoginRequiredMixin, UpdateView):

    model = User
    form_class = EditProfileForm
    template_name = 'self-profile.html'

    def form_valid(self, form):

        self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        context['id'] = self.object.id
        reklamlar = Advertisements.objects.filter(pages ='Self Profile')
        context['reklamlar'] = reklamlar
        print(context['id'])
        return context

  
    def get_object(self):
        return self.request.user


class UserProfilePageView(ListView, LoginRequiredMixin):

    template_name = 'user-profile2.html'
    model = Product

    def get_products(self):
        sale_products = Product.objects.filter(
            user_id=self.request.user.id).all().order_by('-created_at')
        return sale_products

    def get_context_data(self, **kwargs):
        userr_slug = self.kwargs.get('slug')
        user = User.objects.filter(slug=userr_slug).first()
        print(user)
        context = super().get_context_data(**kwargs)
        context['products'] = self.get_products()
        context['user'] = user
        reklamlar = Advertisements.objects.filter(pages ='User Profile')
        context['reklamlar'] = reklamlar
        return context
