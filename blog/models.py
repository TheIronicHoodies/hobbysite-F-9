from django.db import models
from django.urls import reverse

# Create your models here.

class ArticleCategory(models.Model):
    name = models.CharField(max_length = 255)
    # creates field for ArticleCategory name    

    description = models.TextField()
    # creates TextField for description

    class Meta:
        ordering = ['name']
        # sorts categories by ascending order

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('articlecategory', args=[str(self.pk)])

class Article(models.Model):
    title = models.CharField(max_length = 255)
    category = models.ForeignKey(
        ArticleCategory,
        on_delete = models.SET_NULL,
        null=True
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        # sorted by creation date in descending order

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', args=[str(self.pk)])
    
