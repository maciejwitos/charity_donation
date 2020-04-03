"""charity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from charity_donation.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name='landing-page'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('donate/form/', DonationView.as_view(), name='donate-form'),
    path('donate/form/confirmation/', ConfirmationView.as_view(), name='form-confirmation'),
    path('user/profile/', UserProfile.as_view(), name='user-profile'),
    path('user/donations/', UserDonations.as_view(), name='user-donations'),
    path('user/settings/<pk>/', UserSettings.as_view(), name='user-settings'),
    path('user/password_confirm/', ConfirmPasswordView.as_view(), name='confirm-password'),
    path('accounts/password_change', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html',
                                                                           success_url='/accounts/password_change/done/'),
         name='password-change'),
    path('accounts/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password-change-done'),
    path('404/', View404.as_view(), name='404'),

]
