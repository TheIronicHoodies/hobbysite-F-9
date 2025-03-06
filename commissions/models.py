from django.db import models
from django.urls import reverse

class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    people_required = models.IntegerField(null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on',]

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('commission:commissions-detail', args=[str(self.id)])

class Comment(models.Model):
    commission = models.ForeignKey(Commission, null=False, on_delete=models.CASCADE, related_name='comment')
    entry = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on',]

    def __str__(self):
        return str(self.entry)
