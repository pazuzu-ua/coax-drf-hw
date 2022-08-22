from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    """Class that represents a Product."""
    name = models.CharField(
        _('Product name'),
        max_length=35,
    )
    description = models.TextField(
        _('Product description'),
        max_length=400,
    )
    price = models.FloatField(
        _('Product price'),
    )
    created_at = models.DateTimeField(
       _('Created at'), 
       auto_now_add=True,
    )


class Order(models.Model):
    """Class that represents an Order."""
    product = models.ForeignKey(
        'Product',
        related_name=_('Product'),
        on_delete=models.CASCADE,
        )
    created_at = models.DateTimeField(
       _('Created at'), 
       auto_now=True,
    )
