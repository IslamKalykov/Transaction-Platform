from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate_amount(self, value):
        """
        Пользовательская валидация для поля 'amount'.
        Убедитесь, что сумма транзакции больше 0.
        """
        if value <= 0:
            raise serializers.ValidationError("Сумма транзакции должна быть больше 0.")
        return value

    def validate(self, data):
        """
        Общая валидация для проверки условий перед сохранением транзакции.
        """
        amount = data.get('amount', 0)
        source_account = data.get('from_account')
        destination_account = data.get('to_account')

        if amount > source_account.balance:
            raise serializers.ValidationError("Недостаточно средств на счете для проведения транзакции.")

        if not source_account.is_active or source_account.is_blocked:
            raise serializers.ValidationError("Счет отправителя неактивен или заблокирован.")

        if destination_account == source_account:
            raise serializers.ValidationError("Такой перевод невозможен.")

        if source_account.balance - amount < source_account.min_balance:
            raise serializers.ValidationError("Недостаточно средств на счете для проведения транзакции.")

        return data