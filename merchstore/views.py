"""Sets list and detail view of merchstore's list and detail view."""

from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView


class ProductListView(ListView):
    """List view for listing all available products."""

    model = Product
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    """Detail view for listing all the details of a product."""

    model = Product
    template_name = 'product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'


class CartView(ListView):
    model = Product
    template_name = 'cart.html'


class TransactionsListView(ListView):
    model = Product
    template_name = 'transactions.html'