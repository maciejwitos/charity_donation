from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.views import View
from charity_donation.models import *
from charity_donation.forms import *


class LandingPage(View):

    def get(self, request):
        donations = Donation.objects.all()
        institutions_already_donated = Institution.objects.all()
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


class DonationView(LoginRequiredMixin, View):

    login_url = 'login'

    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories,
                                             'institutions': institutions})

    def post(self, request):
        categories = request.POST.get('categories-choose').split(',')
        new_donation = Donation.objects.create(quantity=request.POST.get('bags'),
                                               address=request.POST.get('address'),
                                               city=request.POST.get('city'),
                                               zip_code=request.POST.get('zip_code'),
                                               phone_number=request.POST.get('phone'),
                                               pickup_date=request.POST.get('date'),
                                               pickup_time=request.POST.get('time'),
                                               pickup_comment=request.POST.get('more_info'),
                                               user_id=request.user.pk)
        for category_name in categories:
            new_donation.categories.add(Category.objects.get(name=category_name))
            new_donation.save()
        new_donation.institution.add(Institution.objects.get(name=request.POST.get('institution')).pk)
        new_donation.save()
        return redirect('form-confirmation')


class ConfirmationView(View):

    def get(self, request):
        return render(request, 'form-confirmation.html')


class UserProfile(View):

    def get(self, request):
        return render(request, 'user_profile.html')


class UserDonations(View):

    def get(self, request):
        donations = Donation.objects.filter(user=request.user).order_by('-pickup_date').order_by('collected')
        return render(request, 'user_donations.html', {'donations': donations})