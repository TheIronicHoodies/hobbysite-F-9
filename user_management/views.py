from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .forms import ProfileForm
from .models import Profile

# Create your views here.
class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["profile"] = Profile.objects.get(pk=self.kwargs["pk"])
        return ctx

    def form_valid(self, form):
        form.instance.issue = self.request.user
        return super().form_valid(form)
