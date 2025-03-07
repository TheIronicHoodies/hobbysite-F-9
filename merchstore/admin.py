"""Creates an admin panel for the merchstore app."""

from django.contrib import admin
from .models import Product, ProductType


class ProductInLine(admin.TabularInline):
    """Creates an admin interface managing Product models."""

    model = Product


class ProductTypeAdmin(admin.ModelAdmin):
    """Adds a table for all related Product objects."""

    inlines = [ProductInLine, ]


admin.site.register(ProductType, ProductTypeAdmin)
