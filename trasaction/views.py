from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Transaction
from .serializers import TransactionSerializer
# Create your views here.


class TransactionListView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
