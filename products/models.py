from django.db import models

from categories.models import Categories


class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.00)
    description = models.CharField(max_length=300)
    #image = models.ImageField(upload_to='uploads/products/')
    image = models.CharField(max_length=200, default=None)
    created = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    category = models.ManyToManyField(
        Categories, blank=True)

    def __str__(self):
        return f"{self.name} - £{self.price}"
