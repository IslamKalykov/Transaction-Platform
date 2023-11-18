from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Transaction
from .serializers import TransactionSerializer, AccountSerializer
from account.models import Account
from rest_framework import serializers
# Create your views here.


class AccountTransactionView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        from_account_id = self.request.data.get('from_account')
        to_account_id = self.request.data.get('to_account')

        from_account = Account.objects.get(id=from_account_id)
        to_account = Account.objects.get(id=to_account_id)

        amount = serializer.validated_data['amount']

        if from_account.balance - amount < from_account.min_balance:
            raise serializers.ValidationError("Insufficient funds.")

        from_account.balance -= amount
        from_account.save()

        to_account.balance += amount
        to_account.save()

        serializer.save()


class AccountDetailView(RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
