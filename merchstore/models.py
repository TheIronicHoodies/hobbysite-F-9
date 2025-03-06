from django.db import models
from django.urls import reverse

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('merchstore:productType', args=[str(self.pk)])
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    productType = models.ForeignKey (
        ProductType,
        on_delete=models.SET_NULL,
        related_name='product'
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('merchstore:product', args=[str(self.pk)])