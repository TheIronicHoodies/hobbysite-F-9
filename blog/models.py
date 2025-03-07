from django.db import models
from django.urls import reverse

# Create your models here.

class ArticleCategory(models.Model):
    """
        This creates an ArticleCategory model which orders categories in alphebetic order (ascending)
    """
    
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
        return reverse('blog:category_detail', args=[str(self.pk)])

class Article(models.Model):
    """
        This creates the Article model, which has a title, category, entry text, and created and updated on dates
    """
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
        return reverse('blog:article_detail', args=[str(self.pk)])
    
