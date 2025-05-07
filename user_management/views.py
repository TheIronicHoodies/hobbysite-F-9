from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import Profile

# Create your views here.
class ProfileUpdate(UpdateView):
    model = Profile