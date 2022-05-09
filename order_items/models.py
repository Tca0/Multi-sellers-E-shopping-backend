from django.db import models
from order_details.models import OrderDetails

from products.models import Product


class OrderItems(models.Model):
    order = models.ForeignKey(
        OrderDetails, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id
