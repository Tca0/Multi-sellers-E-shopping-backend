
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from products.models import Product
from products.serializers import ListCreateProductSerializer, ShowProductsListSerializer, UpdateProductSerializer, UpdateQuantityAndProductStatusAfterOrderSerializer
from backend.permissions import IsSeller, IsProductOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# class ShowProductsListView(generics.ListCreateAPIView):
class ShowProductsListView(generics.ListAPIView):
    permission_classes = [IsProductOwner]
    queryset = Product.objects.all()
    serializer_class = ShowProductsListSerializer


class CreateProductsView(generics.ListCreateAPIView):
    # permission_classes = [IsProductOwner]
    # queryset = Product.objects.all().filter()
    serializer_class = ListCreateProductSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return []
        return Product.objects.filter(seller=user)


class ShowProductView(generics.RetrieveUpdateDestroyAPIView):
   # permission_classes = [IsProductOwner]
    queryset = Product.objects.all()
    serializer_class = UpdateProductSerializer

# a view to seller to update their items when receive and order
# class UpdatedInStockAndQuantityView(generics.RetrieveUpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = UpdateQuantityAndProductStatusAfterOrderSerializer
