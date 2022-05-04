from rest_framework import serializers

from .models import Product
#from categories.models import Categories


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def create_product(self, data):
        print(data)
        #product = Product(**data)
        request = self.context.get("request")
        print('request', request)
        # if request and hasattr(request, "user"):
        #    product.seller = request.user
        # product.save()
        return True
