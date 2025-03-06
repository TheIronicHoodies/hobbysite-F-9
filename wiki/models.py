from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('wiki:articles')


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, related_name='articles')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    updated_on = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ["-created_on"]

    def get_absolute_url(self):
        return reverse('wiki:article', args=[self.pk])