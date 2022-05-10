from django.shortcuts import render
from rest_framework import generics

from .serializers import OrderedItemsListSerializer

from .models import OrderItems


class OrderedItemsListView(generics.ListAPIView):
    queryset = OrderItems
    serializer_class = OrderedItemsListSerializer
