from django.db import models
from django.urls import reverse

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('merchstore:productType', args=[str(self.name)])

class Product(models.Model):
    name = models.CharField(max_length=255)
    productType = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
        related_name='productType'
    )
    description = models.TextField
    price = models.DecimalField(decimal_places=2, max_digits=10)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('merchstore:product', args=[str(self.name)])