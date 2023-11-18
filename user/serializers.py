from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed, ValidationError

from user.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate(self, attrs):
        attrs["password"] = make_password(attrs["password"])
        if not attrs["phone"].startswith(("99655", "99675", "99688", "99699", "99622", "996312", "99677", "99650",
                                          "99670", "99660", "99667")):
            raise ValidationError()
        return attrs

    def create(self, validated_data):
        user, _ = User.objects.get_or_create(**validated_data)
        return user


class AuthenticateUserSerializer(serializers.Serializer):
    token = serializers.CharField(read_only=True)
    phone = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.get(phone=validated_data.get("phone"))
        if not check_password(validated_data.get("password"), user.password):
            raise AuthenticationFailed()
        token, _ = Token.objects.get_or_create(user=user)
        return {"token": token.key}
