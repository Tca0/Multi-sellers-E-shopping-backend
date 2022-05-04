
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from products.models import Product
from products.serializers import ProductsSerializer
from backend.permissions import IsSeller, IsProductOwner


class ShowProductsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class CreateProducts(generics.CreateAPIView):
    permission_class = [IsSeller | IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class ShowProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_class = [IsProductOwner | IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
