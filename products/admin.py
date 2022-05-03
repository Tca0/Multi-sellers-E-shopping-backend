from django.contrib import admin

from .models import Product

admin.site.register(Product)


# class ProductAdmin(admin.ModelAdmin):
#list_display = ['name', 'slug', 'seller','price', 'in_stock', 'created_at', 'updated_at']
# list_filter = ['in_stock']
# list_editable = ['price', 'in_stock']
#prepopulated_fields = {'slug': ('name',)}
