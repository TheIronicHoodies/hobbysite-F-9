"""Creates PostCategory and Post models for forum."""

from django.db import models
from django.urls import reverse
from user_management.models import Profile


class ThreadCategory(models.Model):
    #groups of threads
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["name"] #sorts threads alphabetically

    def __str__(self):
        """Returns name of the post category."""

        return self.name


class Thread(models.Model):
    #main discussion thread
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(ThreadCategory, on_delete=models.SET_NULL, null=True, related_name="posts")
    entry = models.TextField()
    image = models.ImageField(upload_to='thread_images/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]  #sorts by oldest

    def __str__(self):
        """Returns the title of the post."""

        return self.title

    def get_absolute_url(self):
        """Returns the absolute URL for a post."""

        return reverse('forum:thread-detail', args=[str(self.id)])

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='forum_comments')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment by {self.author} on {self.thread}"
