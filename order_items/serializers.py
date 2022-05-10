from rest_framework import serializers
from products.models import Product
from .models import OrderItems
from products.serializers import update_quantity_in_stock


class OrderedproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'seller')


class OrderedItemsListSerializer(serializers.ModelSerializer):
    product = OrderedproductSerializer()

    class Meta:
        model = OrderItems
        fields = (
            "product",
            "quantity",
            "price_per_unit",
        )


def create_ordered_items(item, order_number, ordered_product, ordered_quantity):
    print("-------------")
    print("receiving an item from ordered list of items: ",
          item, "\n order number is", order_number)
    #product = item['product']
    quantity = item['quantity']
    print(item['product'], quantity)
    # check if item is available to order(ordered quantity can be served)
    # if it can be mark it as approved true otherwise mark it as refunded

    created_item = OrderItems.objects.create(
        order=order_number, **item, price_per_unit=item['product'].price, subtotal=item['quantity']*item['product'].price)
    if ordered_product.quantity >= ordered_quantity:
        print("ordered item should be accepted")
        created_item.order_item_status = True
        # call update qyt in the db to change the quantity for order
        update_quantity_in_stock(ordered_product, ordered_quantity)
        created_item.save()
        print("created a new item in order_items table ", created_item)
        return created_item
    else:
        created_item.order_item_status = False
        created_item.save()
        print("created a new item in order_items table ", created_item)
        print(item, " This order not replaced")
        print("refund process")
        return created_item
