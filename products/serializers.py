from rest_framework import serializers

from .models import Product
#from categories.models import Categories


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


class CreateProductSerializer(serializers.ModelSerializer):
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
            product.name = data.get('username', product.name)
            product.price = data.get('price', product.price)
            product.description = data.get('description', product.description)
            product.image = data.get('image', product.image)
            product.quantity = data.get('quantity', product.quantity)
            product.in_stock = data.get('in_stock', product.in_stock)
            product.is_active = data.get('is_active', product.is_active)
            product.category = data.get('category', product.category)

            product.save()
            return product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
