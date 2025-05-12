"""Creates ProductType and Product models for merchstore."""

from django.db import models
from django.urls import reverse
from user_management.models import Profile


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
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='owner'
    )
    stock = models.IntegerField()
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sale', 'On sale'),
        ('out of stock', 'Out of stock')
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'
    )

    class Meta:
        """Set the order of data stored in ascending order."""

        ordering = ['name']

    def __str__(self):
        """Return the name of the Product."""
        return self.name

    def get_absolute_url(self):
        """Return the url of the model."""
        return reverse('merchstore:product', args=[str(self.pk)])
    
class Transaction(models.Model):
    buyer = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='buyer'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        related_name='product'
    )
    amount = models.IntegerField()
    STATUS_CHOICES = [
        ('on cart', 'On Cart'),
        ('to pay', 'To Pay'),
        ('to ship', 'To Ship'),
        ('to receive', 'To Receive'),
        ('delivered', 'Delivered')
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
    )
    CreatedOn = models.DateField(auto_created=True)
