from django.contrib import admin
from .models import Product, ProductType
# Register your models here.

class ProductInLine(admin.TabularInline):
    model = Product

class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [ProductInLine,]
    model = ProductType

admin.site.register(ProductType, ProductTypeAdmin)