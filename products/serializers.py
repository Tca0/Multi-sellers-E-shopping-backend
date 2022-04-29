from rest_framework import serializers

from products.models import Products
from categories.models import Categories


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Products
        fields = "__all__"
