from rest_framework import generics
from .serializers import RegisterCustomerSerializer, RegisterVendorSerializer
from users.models import CustomerOrVendor
from backend.permissions import IsSeller


class RegisterCustomerView(generics.CreateAPIView):

    queryset = CustomerOrVendor.objects.all()
    serializer_class = RegisterCustomerSerializer


class BecomeVendorView(generics.CreateAPIView):
    queryset = CustomerOrVendor.objects.all()
    serializer_class = RegisterVendorSerializer
