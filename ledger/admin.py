from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

# Register your models here.

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

# registering the model and the admin is what tells
# Django that admin pages must be generated for the models specified
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)


