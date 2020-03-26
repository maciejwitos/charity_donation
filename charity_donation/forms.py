from django.contrib.auth.forms import UserCreationForm, UserModel
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from charity_donation.models import *


class RegisterForm(UserCreationForm):
    username = forms.EmailField()

    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):

    username = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))




