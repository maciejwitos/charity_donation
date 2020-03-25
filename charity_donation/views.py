from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.views import View
from charity_donation.models import *
from charity_donation.forms import *


class LandingPage(View):

    def get(self, request):
        donations = Donation.objects.all()
        institutions_already_donated = Institution.objects.filter(donation__quantity__gt=0)
        all_institutions = Institution.objects.all()
        bags_qty = 0
        for bags in donations:
            bags_qty += bags.quantity

        return render(request, 'index.html', {'bags_qty': bags_qty,
                                              'institutions_already_donated': institutions_already_donated.count(),
                                              'all_institutions': all_institutions})


class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('landing-page')
        else:
            return redirect('register')


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('landing-page')

class Register(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = RegisterForm()
            return render(request, 'register.html', {'form': form})


class DonationForm(View):

    def get(self, request):
        return render(request, 'form.html')


