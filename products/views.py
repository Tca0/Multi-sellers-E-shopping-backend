
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import GenericAPIView
from products.models import Product
from products.serializers import ShowProductsListSerializer, CreateProductSerializer, UpdateProductSerializer
from backend.permissions import IsSeller, IsProductOwner


# class ShowProductsListView(generics.ListCreateAPIView):
class ShowProductsListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ShowProductsListSerializer


class CreateProductsView(generics.CreateAPIView):
    permission_classes = [IsSeller | IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class ShowProductView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsProductOwner | IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = UpdateProductSerializer
