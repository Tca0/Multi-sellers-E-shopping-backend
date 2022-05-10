from django.db import models
from order_details.models import OrderDetails

from products.models import Product

#ORDERED_ITEM_CHOICES = ('PLACED', 'CANCELLED', 'FALSE')


class OrderItems(models.Model):
    order = models.ForeignKey(
        OrderDetails, related_name='itemsList', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='product', on_delete=models.CASCADE)
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    subtotal = models.DecimalField(
        max_digits=16, decimal_places=2, default=0)
    # change status field name to approved
    order_item_status = models.BooleanField(default=False)

    def __str__(self):
        return self.order.order_number
