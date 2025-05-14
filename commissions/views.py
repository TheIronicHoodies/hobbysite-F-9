from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
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
    
    jobs = [j for j in ]
    slots_filled = 0
    for j in jobs:
        slots_filled += Job.get_manpower()
    slots_left = Job.manpower_required - slots_filled

class CommissionsCreate(CreateView, LoginRequiredMixin):
    model = Commission
    # form_class = pass
    # template_name = pass

class CommissionsUpdate(UpdateView, LoginRequiredMixin):
    model = Commission
    # form_class = pass
    # template_name = pass