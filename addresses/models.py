from django.db import models


class Address(models.Model):
    flat_number = models.CharField(max_length=255)
    building_name = models.CharField(max_length=255)
    building_number = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.country} {self.postcode}-{self.city}"
