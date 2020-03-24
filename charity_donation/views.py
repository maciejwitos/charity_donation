from django.shortcuts import render
from django.views import View
from charity_donation.models import *


class LandingPage(View):

    def get(self, request):
        donations = Donation.objects.all()
        institutions_already_donated = Institution.objects.filter(donation__quantity__gt=0)
        all_institutions = Institution.objects.all()
        print(all_institutions[0].categories.all())
        bags_qty = 0
        for bags in donations:
            bags_qty += bags.quantity

        return render(request, 'index.html', {'bags_qty': bags_qty,
                                              'institutions_already_donated': institutions_already_donated.count(),
                                              'all_institutions': all_institutions})


class Login(View):

    def get(self, request):
        return render(request, 'login.html')


class Register(View):

    def get(self, request):
        return render(request, 'register.html')


class DonationForm(View):

    def get(self, request):
        return render(request, 'form.html')