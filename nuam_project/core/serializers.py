from rest_framework import serializers
from .models import Transaction, ExchangeRate

class TransactionSerializer(serializers.ModelSerializer):
    amount_in_usd = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Transaction
        fields = ['id','description','amount','currency','location','created_at','amount_in_usd']

    def get_amount_in_usd(self, obj):
        val = obj.amount_in_usd()
        return None if val is None else str(val)

class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ['currency','rate_to_usd','updated_at']
