from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomerOrVendor


class RegisterCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrVendor
        fields = ('username', 'password', 'repeat_password', 'email')
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomerOrVendor.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    repeat_password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['repeat_password']:
            raise serializers.ValidationError(
                {"password": "password fields don't match"}
            )
        return attrs

    def create(self, data):
        user = CustomerOrVendor.objects.create(
            username=data['username'],
            email=data['email'],
        )
        user.set_password(data['password'])
        user.save()
        print('unsterilized password which arrived in JSON format from frontend',
              data['password'])
        print('password stored in DB', getattr(user, 'password'))
        return user


class RegisterVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrVendor
        fields = ('username', 'password', 'repeat_password', 'email')
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomerOrVendor.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    repeat_password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['repeat_password']:
            raise serializers.ValidationError(
                {"password": "password fields don't match"}
            )
        return attrs

    def create(self, data):
        user = CustomerOrVendor.objects.create(
            username=data['username'],
            email=data['email'],
        )
        user.set_password(data['password'])
        user.is_vendor = True
        user.is_staff = True
        user.save()
        print('unsterilized password which arrived in JSON format from frontend',
              data['password'])
        print('password stored in DB', getattr(user, 'password'))
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrVendor
        fields = '__all__'
