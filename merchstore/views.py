from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
