from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Transaction
from .serializers import TransactionSerializer, AccountSerializer
from rest_framework.response import Response
from rest_framework import status
from account.models import Account


# Create your views here.


class TransactionListView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        # Получаем данные из запроса
        amount = serializer.validated_data.get('amount')
        from_account = serializer.validated_data.get('from_account')
        to_account = serializer.validated_data.get('to_account')

        # Проверяем, достаточно ли средств на счете отправителя
        if from_account.balance < amount:
            # Если недостаточно средств, устанавливаем статус транзакции в "Неуспешно"
            serializer.save(status="Неуспешно")
            return Response({'error': 'Недостаточно средств на счете отправителя'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Проводим транзакцию (уменьшаем баланс отправителя и увеличиваем баланс получателя)
        from_account.balance -= amount
        to_account.balance += amount
        from_account.save()
        to_account.save()

        # Устанавливаем статус транзакции в "Успешно"
        serializer.save(status="Успешно")

        # Можно добавить дополнительные поля или логику, если нужно

        # Возвращаем успешный ответ
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AccountDetailView(RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer