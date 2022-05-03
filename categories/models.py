from django.db import models
from users.models import CustomerOrVendor


class Category(models.Model):
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(
        CustomerOrVendor, related_name='admin', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
