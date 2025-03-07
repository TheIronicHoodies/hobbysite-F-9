"""Creates PostCategory and Post models for forum."""

from django.db import models
from django.urls import reverse


class PostCategory(models.Model):
    """Creates a PostCategory model following the specs."""

    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        """Set the order of data in ascending order."""

        ordering = ["name"] 

    def __str__(self):
        """Returns name of the post category."""

        return self.name


class Post(models.Model):
    """Creates a Post model following the specs."""

    title = models.CharField(max_length=255)
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True, related_name="posts")
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Set the order of data in descending order."""

        ordering = ["-created_on"] 

    def __str__(self):
        """Returns the title of the post."""

        return self.title

    def get_absolute_url(self):
        """Returns the absolute URL for a post."""

        return reverse('forum:thread-detail', args=[str(self.id)])

