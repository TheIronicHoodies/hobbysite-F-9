"""Sets list and detail view of merchstore's list and detail view."""

from .models import Product, Transaction, ProductType
from .forms import TransactionForm, CreateProduct, UpdateProduct
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class ProductListView(ListView):
    """List view for listing all available products."""

    model = Product
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        product_types = ProductType.objects.all()
        
        context['type_list'] = product_types
        return context


class ProductDetailView(DetailView):
    """Detail view for listing all the details of a product."""

    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = TransactionForm()
        return ctx

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = TransactionForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['amount'] > self.object.stock:
                return redirect('merchstore:product-list')
            if not request.user.is_authenticated:
                return redirect('accounts:login')
            transaction = form.save(commit=False)
            transaction.product = self.object
            transaction.buyer = self.request.user.profile
            self.object.stock -= form.cleaned_data['amount']
            if self.object.stock == 0:
                self.object.status = 'out of stock'
            self.object.save()
            transaction.save()
            return redirect('merchstore:cart')
        return self.render_to_response(self.get_context_data(form=form))


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
    context_object_name = 'cart'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        product_types = ProductType.objects.all()
        
        context['type_list'] = product_types
        return context

    def get_queryset(self):
        return Transaction.objects.filter(buyer=self.request.user.profile)


class TransactionsListView(ListView):
    model = Transaction
    template_name = 'transactions.html'
    context_object_name = 'transactions'
