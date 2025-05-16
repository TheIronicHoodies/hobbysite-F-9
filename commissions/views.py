from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .forms import *
from .models import Commission, Job

# Create your views here.
class CommissionsList(ListView):
    model = Commission
    template_name = 'commissions_list.html'


class CommissionsDetail(DetailView, FormMixin):
    model = Commission
    template_name = 'commissions_detail.html'
    redirect_field_name = '/accounts/login'
    form_class = JobApplicationForm
    
    def post(self, request, *args, **kwargs):
        ja = JobApplication()
        ja.job = Commission.jobs.job.get('job')
        ja.applicant = self.request.user.profile
        ja.status = 'Pending'
        ja.save()
        return self.get(request, *args, **kwargs)


class CreateCommission(CreateView, LoginRequiredMixin):
    model = Commission
    form_class = CommissionForm
    form_class.base_fields['author'].disabled = True
    template_name = 'commissions_create.html'
    redirect_field_name = '/accounts/login'
            

class UpdateCommission(UpdateView, LoginRequiredMixin):
    model = Commission
    form_class = CommissionUpdateForm
    form_class.base_fields['author'].disabled = True
    template_name = 'commissions_update.html'
    
    def get(self, request, *args, **kwargs):
        affected_commission = get_object_or_404(Commission, pk=self.kwargs["pk"])
        if request.user.profile != affected_commission.author:
            return redirect(reverse_lazy("commissions:commission_list"))
        return super().get(request, *args, **kwargs)


class CreateJob(CreateView, LoginRequiredMixin):
    model = Job
    form_class = JobForm
    template_name = 'commissions_create.html'
    
    
class UpdateJob(UpdateView, LoginRequiredMixin):
    model = Job
    form_class = JobForm
    template_name = 'commissions_update.html'
