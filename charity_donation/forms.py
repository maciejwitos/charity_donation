from django.contrib.auth.forms import UserCreationForm, UserModel
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from charity_donation.models import *
from django.contrib.auth.hashers import check_password


class RegisterForm(UserCreationForm):
    username = forms.EmailField()

    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):

    username = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))


class ConfirmPasswordForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['confirm_password']

    def clean(self):
        cleaned_data = super(ConfirmPasswordForm, self).clean()
        confirm_password = cleaned_data.get('confirm_password')
        if not check_password(confirm_password, self.instance.password):
            self.add_error('confirm_password', 'Password does not match.')



