from django.db import models
from django.urls import reverse
from hobbysite.models import Profile


class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["name"] 

    def __str__(self):
        return self.name


class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(ThreadCategory, on_delete=models.SET_NULL, null=True, related_name="posts")
    entry = models.TextField()
    image = models.ImageField(upload_to='thread_images/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"] 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:thread-detail', args=[str(self.id)])
    
class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment by {self.author} on {self.thread}"
