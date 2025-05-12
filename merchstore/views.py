"""Sets list and detail view of merchstore's list and detail view."""

from .models import Product, Transaction
from .forms import TransactionForm, CreateProduct, UpdateProduct
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    """List view for listing all available products."""

    model = Product
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    """Detail view for listing all the details of a product."""

    model = Product
    form_class = TransactionForm
    template_name = 'product_detail.html'
    #def get_context_data(self, **kwargs):
    #    ctx = super().get_context_data(**kwargs)
    #    ctx['form'] = TransactionForm()
    #    return ctx

    #def post(self, request, *args, **kwargs):
    #    self.object = self.get_object()
    #    form = TransactionForm(request.POST)
    #    if form.is_valid():
    #        transaction = form.save(commit=False)
    #        transaction.product = self.object
    #        transaction.buyer = request.user.profile
    #       transaction.status = 'on cart'
    #        transaction.save()
    #        return redirect('merchstore:product', pk=self.object.pk)
    #    return self.render_to_response(self.get_context_data(form=form))


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = CreateProduct
    template_name = 'product_create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = UpdateProduct
    template_name = 'product_update.html'
    redirect_field_name = 'product_list.html'

    def form_valid(self, form):
        if form.instance.stock == 0:
            form.instance.status = 'out of stock'
        elif form.instance.stock != 0 and form.instance.status == 'out of stock':
            form.instance.status = 'available'
        return super().form_valid(form)


class CartView(ListView):
    model = Transaction
    template_name = 'cart.html'


class TransactionsListView(ListView):
    model = Transaction
    template_name = 'transactions.html'