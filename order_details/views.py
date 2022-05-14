from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from order_details.models import OrderDetails
from order_details.serializers import MyOrdersListSerializer, ReplaceOrderSerializer
from users.models import CustomerOrVendor
from rest_framework.permissions import IsAuthenticated


class MyOrdersListView(generics.ListAPIView):
    print("viewing my orders list")
    permission_classes = [IsAuthenticated]

    def get(self, request):
        customer_orders = OrderDetails.objects.filter(
            customer=self.request.user)
        serializer = MyOrdersListSerializer(customer_orders, many=True)

        return Response(serializer.data)


class ReplaceCustomerOrdersListView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = OrderDetails
    serializer_class = ReplaceOrderSerializer
