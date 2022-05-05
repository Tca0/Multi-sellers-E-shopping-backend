from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomerOrVendor
#from addresses.serializers import AddressSerializer
from addresses.models import Address
#from dj_rest_auth.registration.serializers import RegisterSerializer
# Define transaction.atomic to rollback the save operation in case of error
#from django.db import transaction


class RegisterUserSerializer(serializers.ModelSerializer):
    # in front end when non-register user navigate to open a store then will attach is_vendor=true to the register request
    # both users will have same route in back end to register but the form for vendors will have extra fields so
    # it should be entered manually for testing it and should be attached in the form by front end.
    class Meta:
        model = CustomerOrVendor
        #fields = ('username', 'password', 'repeat_password', 'email', 'phone_number', 'is_vendor', 'is_staff')
        fields = ('username', 'password', 'repeat_password',
                  'email', 'phone_number', 'is_vendor')
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
        user_password = data.pop('password')
        repeat_password = data.pop('repeat_password')
        phone_number = data.pop("phone_number")
        print(user_password, repeat_password, phone_number)
        print("remain data", data)
        user = CustomerOrVendor.objects.create(**data)
        user.set_password(user_password)
        user.phone_number = phone_number
        user.save()
        print('unsterilized password which arrived in JSON format from frontend',
              user_password)
        print('password stored in DB', getattr(user, 'password'))
        return user


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class UpdateUserSerializer(serializers.ModelSerializer):
    address = UserAddressSerializer()

    class Meta:
        model = CustomerOrVendor
        fields = ('username', 'first_name', 'last_name',
                  'phone_number', 'address')

    def update(self, user, data):
        address_data = data.pop('address')
        print('address is:  ', address_data)
        print('remain data', data)
        user.username = data.get('username', user.username)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.phone_number = data.get('phone_number', user.phone_number)
        if address_data:
            address, _newAddress = Address.objects.get_or_create(
                **address_data)
            user.address = address
        return user


class ViewUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrVendor
        fields = ('first_name', 'last_name', 'username')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrVendor
        fields = '__all__'
