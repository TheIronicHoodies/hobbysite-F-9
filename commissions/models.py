from django.db import models

class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    people_required = models.IntegerField(null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on',]

class Comment(models.Model):
    commission = models.ForeignKey(Commission, null=False, on_delete=models.CASCADE)
    entry = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on',]
