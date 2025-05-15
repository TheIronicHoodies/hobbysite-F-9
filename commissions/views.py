from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import *
from .models import Commission, Job

# Create your views here.
class CommissionsList(ListView):
    model = Commission
    template_name = 'commissions_list.html'


class CommissionsDetail(DetailView):
    model = Commission
    template_name = 'commissions_detail.html'
    redirect_field_name = '/accounts/login'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["commission"] = Commission.objects.get(pk=self.kwargs["pk"])
        return ctx


class CommissionsCreate(CreateView, LoginRequiredMixin):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions_create.html'

    def form_valid(self, form):
        commission = form.save(commit=False)
        commission.author = self.request.user.profile
        commission.save()
        return super().form_valid(form)

class CommissionsUpdate(UpdateView, LoginRequiredMixin):
    model = Commission
    form_class = CommissionUpdateForm
    template_name = 'commissions_update.html'
    
    def get(self, request, *args, **kwargs):
        affected_commission = get_object_or_404(Commission, pk=self.kwargs["pk"])
        if request.user.profile != affected_commission.author:
            return redirect(reverse_lazy("commissions:commission_list"))
        return super().get(request, *args, **kwargs)