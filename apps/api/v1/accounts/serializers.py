from rest_framework import serializers

from apps.accounts.models import User
from phonenumber_field.serializerfields import PhoneNumberField

from apps.accounts.services import get_user


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=128, required=True)
    password = serializers.CharField(max_length=32, required=True, write_only=True)
    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=30, required=True)
    phone_number = PhoneNumberField(max_length=30, required=False)

    def validate_email(self, email):
        if get_user(username=email):
            raise serializers.ValidationError("El email ya se encuenta registrado")
        return email

    def validate_phone_number(self, phone_number):
        if get_user(phone_number=phone_number):
            raise serializers.ValidationError(
                "El número de teléfono ya se encuenta registrado"
            )
        return phone_number
