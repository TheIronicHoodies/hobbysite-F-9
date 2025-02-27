from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

# Register your models here.
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline,]


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
