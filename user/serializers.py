from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from user.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate(self, attrs):
        attrs["password"] = make_password(attrs["password"])
        return attrs

    def create(self, validated_data):
        user, _ = User.objects.get_or_create(**validated_data)
        return user
