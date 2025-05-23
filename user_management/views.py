from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .forms import *
from .models import Profile

# Create your views here.
class ProfileCreate(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = "registration/register.html"

class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "profile_update.html"

    def get_object(self):
        return self.request.user.profile

    def form_valid(self, form):
        form.instance.issue = self.request.user
        return super().form_valid(form)
