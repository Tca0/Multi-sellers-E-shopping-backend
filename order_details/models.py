from django.db import models
from users.models import CustomerOrVendor


class OrderDetails(models.Model):
    order_number = models.CharField(max_length=100, blank=True, null=True)
    customer = models.ForeignKey(CustomerOrVendor, related_name="orders", null=True,
                                 blank=True, default=None, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=500, blank=True, null=True)
    total_amount = models.DecimalField(
        max_digits=20, decimal_places=2, default=0.00)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True,)

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return self.order_number
