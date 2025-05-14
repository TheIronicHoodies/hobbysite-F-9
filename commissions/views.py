from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import Commission, Job

# Create your views here.
class CommissionsList(ListView):
    model = Commission
    template_name = 'commissions_list.html'


class CommissionsDetail(DetailView):
    model = Commission
    template_name = 'commissions_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["commission"] = Commission.objects.get(pk=self.kwargs["pk"])
        return ctx


class CommissionsCreate(CreateView, LoginRequiredMixin):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions_create.html'

class CommissionsUpdate(UpdateView, LoginRequiredMixin):
    model = Commission
    form_class = CommissionUpdateForm
    template_name = 'commissions_update.html'