from rest_framework import permissions


class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        print(request.user.is_vendor)
        return request.user.is_vendor and request.user.is_authenticated


class IsProductOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.seller == request.user and request.user.is_authenticated


class IsCurrentUserWithRightRequest(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return object.username == request.user and request.user.is_authenticated
