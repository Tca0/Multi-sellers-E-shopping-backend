
from rest_framework import generics

from products.models import Product
from products.serializers import ProductsSerializer


class ShowProductsList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class ShowProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
