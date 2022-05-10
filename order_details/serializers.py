from rest_framework import serializers
from order_items.models import OrderItems
from products.models import Product
from .models import OrderDetails
from products.serializers import update_quantity_in_stock
from order_items.serializers import create_ordered_items


class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'seller')


class OrderedItemsListSerializer(serializers.ModelSerializer):
    product = OrderedProductSerializer()

    class Meta:
        model = OrderItems
        fields = ("product", "price_per_unit", "quantity",
                  "subtotal", "order_item_status",)


class MyOrdersListSerializer(serializers.ModelSerializer):
    print("orders list serializers")
    itemsList = OrderedItemsListSerializer(many=True)

    class Meta:
        model = OrderDetails
        fields = ("order_number", "shipping_address",
                  "itemsList", "total_amount")


# replace order functionally:
#   1- frontend send list of items with a unique code (order_number) and shipping address
#   2- backend will store order details in order_details table
#   3- backend will set order items in order_items table and connect it to the unique order number
#   4- backend will reduce the quantity for each product by the quantity that sent by order

class ReplaceOrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ("product", "quantity")


class ReplaceOrderSerializer(serializers.ModelSerializer):
    print("Replace order serializer")
    itemsList = ReplaceOrderItemsSerializer(many=True)

    class Meta:
        model = OrderDetails
        fields = ("order_number", "shipping_address",
                  "itemsList", "total_amount")

    def create(self, data):
        total_amount = 0
        order_items = data.pop("itemsList")
        order = OrderDetails.objects.create(**data)
        order.customer = self.context['request'].user

        print("-------------")
        print("ReplaceOrderSerializer:", "\noreder", order)
        for item in order_items:
            print("passing ", item, " to orderItems table")

            ordered_product = item['product']
            ordered_quantity = item['quantity']
            print("ordered product", ordered_product,
                  "ordered quantity", ordered_quantity)

            # first check stock for ordered quantity if available store the ordered item
            # update_quantity_in_stock will return the updated product or false if ordered quantity not available
            ordered_item = create_ordered_items(
                item, order, ordered_product, ordered_quantity)
            if ordered_item.order_item_status:
                total_amount = + ordered_item.subtotal
                print("total amount after replacing ",
                      item, "is ", total_amount)
                print("---finshing item----")

            print("Total amount now is : ", total_amount)

            order.total_amount = total_amount
            order.save()
        return order
