from django.shortcuts import render
from rest_framework import generics

from user.serializers import RegisterUserSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer


class LoginUserAPIView(generics.CreateAPIView):
    serializer_class = AuthenticateUserSerializer
