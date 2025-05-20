from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Profile


class ProfileCreateForm(UserCreationForm):
    name = forms.CharField(max_length=24)
    email_address = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "name",
            "email_address",
        )

    def save(self, *args, **kwargs):
        # First, save the user
        user = super().save(*args, **kwargs)
        # Then, create the profile
        profile = Profile.objects.create(
            user=user,
            name=self.cleaned_data.get("name"),
            email_address=self.cleaned_data.get("email_address"),
        )

        return profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "email_address",]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
