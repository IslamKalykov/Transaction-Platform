from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import Account
from user.models import User


class CreateAccountAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.META.get('HTTP_AUTHORIZATION').split(' ', 1)[1])
        user = User.objects.get(id=token.user_id)
        Account.objects.get_or_create(user=user, **request.data)
        return Response(
            {"details": f"Account was created"},
            status=status.HTTP_201_CREATED,
        )
