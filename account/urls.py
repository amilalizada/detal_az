from django.urls import path
from account.views import *

app_name = 'account'

urlpatterns = [
    path('/login',LoginPageView.as_view(),name='login'),
    path('/register',RegisterPageView.as_view(),name='register'),
    path('/self-profile',SelfProfilePageView.as_view(),name='self-profile'),
    path('/user-profile',UserProfilePageView.as_view(),name='user-profile'),
    
]