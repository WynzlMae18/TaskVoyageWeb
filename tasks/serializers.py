from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from djoser.serializers import UserCreateSerializer, ActivationSerializer


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        write_only=True)  # Add confirm_password field

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username',
                  'email', 'password', 'confirm_password', 'verified']

    def create(self, validated_data):
        # Remove confirm_password from validated_data
        print(str(validated_data))
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def validate(self, attrs):
        # Remove confirm_password from attrs
        confirm_password = attrs.pop('confirm_password')
        user = CustomUser(**attrs)
        password = attrs.get('password')

        if confirm_password != password:
            raise serializers.ValidationError(
                {'confirm_password': 'Passwords do not match'+str(confirm_password)})

        try:
            validate_password(password, self.instance)
        except DjangoValidationError as e:
            raise serializers.ValidationError({'password': str(e)})

        return attrs


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class EmailConfirmationSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
