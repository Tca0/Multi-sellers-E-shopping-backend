from rest_framework import serializers

from order_items.models import OrderItems
from .models import OrderDetails


class OrderItemsSerializer(serializers.ModelSerializer):
    model = OrderItems
    fields = ("product", "price", "quantity")


class OrderSerializer(serializers.ModelSerializer):
    itemsList = OrderItemsSerializer(many=True)

    class Meta:
        model = OrderDetails
        #fields = ("order_number", "shipping_address", "itemsList")
        fields = '__all__'

    def create(self, data):
        print("incoming data", data)
        order_items = data.pop("itemsList")
        order = OrderDetails.objects.create(**data)
        order.save()
        for item in order_items:
            OrderItems.objects.create(order=order, **item)
        return order
