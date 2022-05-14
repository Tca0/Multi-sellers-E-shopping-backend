# from requests import Response
from rest_framework.response import Response

from rest_framework import serializers

from .models import Product
# from categories.models import Categories


class ShowProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def in_stock_and_active_products(self):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            print('checking request from?', request.user.username)
            if request.user.is_vendor:
                return Product.objects.filter(
                    is_vendor=request.user.is_vendor)
            if request.user.is_staff:
                return Product.objects.all().order_by('seller')
        else:
            return Product.objects.all().order_by('category')

    def create(self, data):
        return
        request = self.context.get("request")
        if request and hasattr(request, "user") and request.user.is_vendor or request.user.is_staff:
            new_product = Product.objects.create(**data)
            if request.user.is_vendor:
                new_product.seller = request.user
            new_product.save()
            return new_product


class ListCreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def create(self, data):
        request = self.context.get("request")
        new_product = Product.objects.create(**data)
        if request and hasattr(request, "user"):
            new_product.seller = request.user
        new_product.save()
        return new_product


class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'image',
                  'quantity', 'in_stock', 'is_active', 'category')

        def update(self, product, data):
            product.name = data.get('name', product.name)
            product.price = data.get('price', product.price)
            product.description = data.get('description', product.description)
            product.image = data.get('image', product.image)
            product.quantity = data.get('quantity', product.quantity)
            product.in_stock = data.get('in_stock', product.in_stock)
            product.is_active = data.get('is_active', product.is_active)
            product.category = data.get('category', product.category)

            product.save()
            return product


class UpdateQuantityAndProductStatusAfterOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('quantity',)

    def update_quantity(self, product, data):
        print("product to update after an order", product)
        print("reduce by", data.get('quantity'))
        if product.quantity > 0:
            product.quantity -= data.get('quantity')
        if product.quantity <= 0:
            print("quantity 0, out of stock")
            product.is_active = False
            product.in_stock = False
        product.save()
        return product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


def update_quantity_in_stock(product, ordered_quantity):
    print("----------------")
    print("product update quantity function in product.serializers")
    print("update qty fun in product serializer",
          "\n product to update after an order", product)
    print("product qty in db", product.quantity)
    print("ordered item should be accepted")
    print("quantity in db reduce by", ordered_quantity)
    product.quantity -= ordered_quantity
    print("new qyt in db:", product.quantity)

    print("\n checking if product now is out of stock")
    if product.quantity <= 0:
        print("quantity 0, out of stock")
        product.is_active = False
        product.in_stock = False
    product.save()
    return product
