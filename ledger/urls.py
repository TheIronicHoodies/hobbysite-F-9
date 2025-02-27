from django.urls import path
from .views import RecipesList, RecipesDetail

urlpatterns = [
    path('recipes/list', RecipesList.as_view(), name='recipes-list'),
    path('recipe/<int:pk>', RecipesDetail.as_view(), name='recipes-detail')
]

app_name = 'ledger'
