from django.db import models
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    '''Represents an ingredient in the recipe.'''
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        '''Returns absolute url to this ingredient's page.'''
        return reverse('ingredient', args=[str(self.pk)])
    
    class Meta:
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'


class Recipe(models.Model):
    '''Represents a dish.'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        '''Returns absolute url to this recipe.'''
        return reverse('recipe', args=[self.pk])
    
    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'


class RecipeIngredient(models.Model):
    '''Represents a list of ingredients used to create a dish.'''
    quantity = models.IntegerField()
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        null=False,
        related_name='recipe'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        null=False,
        related_name='ingredients'
    )

    class Meta:
        verbose_name = 'recipe_ingredient'
        verbose_name_plural = 'recipe_ingredients'
