from django.contrib.auth.models import User
from rest_framework import serializers

from categories.models import Category


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AddCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)

    def create(self, data):
        print(User.pk)
        new_category = Category.objects.create(**data)
        new_category.created_by = User
        return new_category
