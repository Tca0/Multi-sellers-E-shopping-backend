from django.db import models


class Store(models.Model):
    store_name = models.CharField(max_length=50)
