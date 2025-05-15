from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class ProfileCreateForm(UserCreationForm):
    name = forms.CharField(max_length=24)
    email_address = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1','password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "email_address",]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
