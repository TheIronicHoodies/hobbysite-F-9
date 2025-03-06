from django.contrib import admin
from .models import Product, ProductType
# Register your models here.

class ProductTypeInLine(admin.TabularInline):
    model = ProductType

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductTypeInLine,]

admin.site.register(Product, ProductAdmin)