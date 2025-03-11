from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

class RecipesList(ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipesDetail(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    redirect_field_name = '/accounts/login'
