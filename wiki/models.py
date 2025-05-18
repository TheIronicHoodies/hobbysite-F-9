from django.db import models
from django.urls import reverse
from user_management.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('wiki:articles')

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, related_name='articles',)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='wiki_articles') #we will work this out
    entry = models.TextField()
    header_image = models.ImageField(null=True, upload_to='images/') #not too much of an issue
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    updated_on = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ["-created_on"]

    def get_absolute_url(self):
        return reverse('wiki:article', args=[self.pk])
    
    def __str__(self):
        return f'{self.title}'
    
    
class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='wiki_comments') #we will work this out
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, related_name='comments',)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    updated_on = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ["created_on"]
        
    def get_absolute_url(self):
        return reverse('wiki:article', args=[self.article.pk])
    
    def __str__(self):
        return f'{self.article}: {self.entry}'
    

class ImageGallery(models.Model):
    image = models.ImageField(null=False, upload_to='images/')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False, related_name='gallery')
    
    def get_absolute_url(self):
        return reverse('wiki:article', args=[self.article.pk])
    