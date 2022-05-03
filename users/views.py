from rest_framework import generics
from .serializers import RegisterCustomerSerializer
from users.models import CustomerOrVendor


class RegisterCustomerView(generics.CreateAPIView):
    queryset = CustomerOrVendor.objects.all()
    serializer_class = RegisterCustomerSerializer
