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
        verbose_name = 'commission'
        verbose_name_plural = 'commissions'

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('commissions:commissions-detail', args=[str(self.id)])

class Comment(models.Model):
    commission = models.ForeignKey(Commission, null=False, on_delete=models.CASCADE, related_name='comments')
    entry = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on',]
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return str(self.entry)
