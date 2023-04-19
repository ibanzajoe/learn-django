from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user"""

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # list all fields that may possibly be included in a request
        # or response, including fields specified explicitly above
        fields = ["email", "username", "password", "token"]

    def create(self, validated_data):
        # Use the model method: `create_user` to create new user
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if email is None:
            raise serializers.ValidationError("An email address is required to log in.")

        if password is None:
            raise serializers.ValidationError("A password is required to log in")

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                "A user with this email and password was not found."
            )

        if not user.is_active:
            raise serializers.ValidationError("This user has been deactivated")

        # the 'validate' method should return a dictionary of validated data
        # This is the data that is passed to the 'create' and 'update' methods
        return {"email": user.email, "username": user.username, "token": user.token}


class UserSerializer(serializers.Serializer):
    """Handles serialization and deserialization of User objects."""

    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=128)
    last_name = serializers.CharField(max_length=128)

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "password",
            "token",
        )

        read_only_fields = "token"

    def update(Self, instance, validated_data):
        """Update User"""

        password = validated_data.pop("password", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance
