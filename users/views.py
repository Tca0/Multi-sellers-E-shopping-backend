from rest_framework import generics
from .serializers import RegisterUserSerializer, UpdateUserSerializer, ViewUserInfoSerializer
from users.models import CustomerOrVendor
from backend.permissions import IsCurrentUserWithRightRequest
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class RegisterView(generics.CreateAPIView):

    queryset = CustomerOrVendor.objects.all()
    serializer_class = RegisterUserSerializer


class UserUpdateDeleteProfileView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser |
                          IsCurrentUserWithRightRequest and IsAuthenticated]
    queryset = CustomerOrVendor.objects.all()
    serializer_class = UpdateUserSerializer


class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = CustomerOrVendor.objects.all()
    serializer_class = ViewUserInfoSerializer
