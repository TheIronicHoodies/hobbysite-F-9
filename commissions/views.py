from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Commission

# Create your views here.
class CommissionsList(ListView):
    model = Commission
    template_name = 'commissions_list.html'

class CommissionsDetail(DetailView):
    model = Commission
    template_name = 'commissions_detail.html'

class CommissionsCreate(CreateView):
    model = Commission
    form_class = pass
    template_name = pass

class CommissionsUpdate(UpdateView):
    model = Commission
    form_class = pass
    template_name = pass