from django.db import models
from django.contrib.auth.models import AbstractUser
from addresses.models import Address


class CustomerOrVendor(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    #is_customer = models.BooleanField(default=False)
    address = models.OneToOneField(
        Address, related_name='address', null=True, blank=True, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
