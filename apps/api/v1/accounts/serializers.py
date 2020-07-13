from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.accounts.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name", "phone_number")
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, email):
        if User.objects.filter(username=email).exists():
            raise serializers.ValidationError("El email ya se encuenta registrado")
        return email

    def validate_phone_number(self, phone_number):

        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError(
                "El número de teléfono ya se encuenta registrado"
            )
        return phone_number

    def create(self, validated_data):
        validated_data["username"] = validated_data["email"]
        return super().create(validated_data)

    def validate_password(self, password):
        return make_password(password)
