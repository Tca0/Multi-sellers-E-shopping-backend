from rest_framework import generics
from .serializers import StoreSerializer
from .models import Store


class ShowStoresList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class ShowStore(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
