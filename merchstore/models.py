"""Creates ProductType and Product models for merchstore."""

from django.db import models
from django.urls import reverse


class ProductType(models.Model):
    """Create the ProductType model according to the specs."""

    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        """Set the order of data stored in ascending order."""

        ordering = ['name']

    def __str__(self):
        """Return the name of the ProductType."""
        return self.name

    def get_absolute_url(self):
        """Return the url of the model."""
        return reverse('merchstore:productType', args=[str(self.pk)])


class Product(models.Model):
    """Create the Product model according to the specs."""

    name = models.CharField(max_length=255)
    ProductType = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True,
        related_name='product'
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """Set the order of data stored in ascending order."""

        ordering = ['name']

    def __str__(self):
        """Return the name of the Product."""
        return self.name

    def get_absolute_url(self):
        """Return the url of the model."""
        return reverse('merchstore:product', args=[str(self.pk)])
