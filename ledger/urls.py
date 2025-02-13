from django.urls import path
from .views import recipes_list, recipe_one, recipe_two

urlpatterns = [
    path('recipes/list', recipes_list, name='recipes-list'),
    path('recipe/1', recipe_one, name='recipe-one'),
    path('recipe/2', recipe_two, name='recipe-two')
]

app_name = 'ledger'