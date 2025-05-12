"""Sets paths to merchstore's list and detail view."""

from django.urls import path
from .views import( 
    ProductListView, ProductDetailView, ProductCreateView, 
    ProductUpdateView, CartView, TransactionsListView
)


urlpatterns = [
    path('merchstore/items', ProductListView.as_view(), name='product-list'),
    path('merchstore/item/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('merchstore/item/add', ProductCreateView.as_view(), name='add-product'),
    path('merchstore/item/<int:pk>/edit', ProductUpdateView.as_view(), name='product-update'),
    path('merchstore/cart', CartView.as_view(), name='cart'), 
    path('merchstore/transactions', TransactionsListView.as_view(), name='transactions')
]

app_name = "merchstore"
