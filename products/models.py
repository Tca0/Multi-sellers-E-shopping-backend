from django.db import models
#from django.urls import reverse
from categories.models import Category
#from vendor.models import Vendor
#from django.contrib.auth.models import User
from users.models import CustomerOrVendor


class Product(models.Model):
    name = models.CharField(max_length=50)
    #slug = models.SlugField(max_length=50, blank=True, null=True)
    price = models.FloatField(default=0.00)
    description = models.TextField(max_length=300, blank=True, null=True)
    # for handling images needs to create different table as a product album
    # one to many relationship and installing pillow package to handle working with images
    #""""SOME ARTICLES SPEAK ABOUT ADDING STATIC URLS , MEDIA URLS & MEDIA ROOT"""""
    # CHECK IT WITH THE TEACHER FOR MORE INFORMATION
    #image = models.ImageField(upload_to='uploads/products/')
    image = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, related_name='category', null=True, blank=True, default=None, on_delete=models.DO_NOTHING)
    # delete store will delete all products
    # It can be referred to user that created it, after setting the store as user_admin
    seller = models.ForeignKey(CustomerOrVendor, related_name="seller", null=True,
                               blank=True, default=None, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=False)

    # class Meta:
    # not necessary to have it because django makes it plural and it will not effect on spelling
    #verbose_name_plural = 'Products'
    # ordering = ('-created_at',)  # ordering decending order

    def __str__(self):
        return f"{self.name} - £{self.price}"

    # def get_absolute_url(self):
        return reverse('vendor:product_detail', args=[self.slug])
