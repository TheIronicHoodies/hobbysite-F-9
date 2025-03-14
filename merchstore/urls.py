"""Sets paths to merchstore's list and detail view."""

from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('merchstore/items', ProductListView.as_view(), name='product-list'),
    path('merchstore/item/<int:pk>', ProductDetailView.as_view(), name='product')
]

app_name = "merchstore"
