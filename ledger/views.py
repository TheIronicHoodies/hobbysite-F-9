from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

class RecipesList(ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipesDetail(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'