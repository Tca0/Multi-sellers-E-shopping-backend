from rest_framework import generics
from .serializers import CategoriesSerializer
from .models import Category


class ShowCategoriesList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class ShowCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
