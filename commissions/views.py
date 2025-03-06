from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Commission

# Create your views here.
class CommissionsList(ListView):
    model = Commission
    template_name = 'commissions_list.html'

class CommissionsDetail(DetailView):
    model = Commission
    template_name = 'commissions_detail.html'