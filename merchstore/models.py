from django.db import models

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField

    class Meta:
            ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=255)
    productType = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
        related_name='ProductType'
    )
    description = models.TextField
    price = models.DecimalField(decimal_places=2)
    
    class Meta:
            ordering = ['name']