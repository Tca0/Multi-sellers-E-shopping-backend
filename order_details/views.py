from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from order_details.models import OrderDetails
from order_details.serializers import OrderSerializer
from users.models import CustomerOrVendor
from rest_framework.permissions import IsAuthenticated


class CustomerOrdersListView(generics.ListAPIView):
    #queryset = OrderDetails.objects.filter(user=request.user)
    #serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(self.request.user)
        print(self.request.user.id)
        customer_orders = OrderDetails.objects.filter(
            customer=self.request.user)
        serializer = OrderSerializer(customer_orders, many=True)

        return Response(serializer.data)


class CustomerOrderView(generics.ListCreateAPIView):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderSerializer
    print("hitting create order")
