from rest_framework import generics
from .serializers import AddCategorySerializer, CategoriesSerializer
from .models import Category
from rest_framework.permissions import IsAdminUser


class ShowCategoriesList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class ShowCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class AddCategory(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = AddCategorySerializer
