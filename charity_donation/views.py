from django.shortcuts import render
from django.views import View
from charity_donation.models import *


class LandingPage(View):

    def get(self, request):
        donations = Donation.objects.all()
        institutions = Institution.objects.filter(donation__quantity__gt=0)
        bags_qty = 0
        for bags in donations:
            bags_qty += bags.quantity

        return render(request, 'index.html', {'bags_qty': bags_qty,
                                              'institution': institutions.count()})


class Login(View):

    def get(self, request):
        return render(request, 'login.html')


class Register(View):

    def get(self, request):
        return render(request, 'register.html')


class DonationForm(View):

    def get(self, request):
        return render(request, 'form.html')