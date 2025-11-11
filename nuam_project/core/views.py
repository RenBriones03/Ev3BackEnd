from rest_framework import viewsets
from .models import Transaction, ExchangeRate
from .serializers import TransactionSerializer, ExchangeRateSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from decimal import Decimal
from core.models import ExchangeRate

def home_view(request):
    rates = ExchangeRate.objects.all()
    return render(request, "core/home.html", {"rates": rates})


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-created_at')
    serializer_class = TransactionSerializer

class ExchangeRateViewSet(viewsets.ModelViewSet):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer

    @action(detail=False, methods=['get'])
    def convert(self, request):
        amount = request.query_params.get('amount')
        from_curr = request.query_params.get('from')
        to_curr = request.query_params.get('to')
        if not (amount and from_curr and to_curr):
            return Response({"detail":"provide amount, from, to"}, status=400)
        try:
            amount = Decimal(amount)
        except:
            return Response({"detail":"invalid amount"}, status=400)

        rates = {r.currency: r.rate_to_usd for r in ExchangeRate.objects.all()}
        if from_curr not in rates or to_curr not in rates:
            return Response({"detail":"currency not found"}, status=404)
        amount_in_usd = amount * rates[from_curr]
        amount_in_to = (amount_in_usd / rates[to_curr]).quantize(Decimal('0.01'))
        return Response({
            "from": from_curr,
            "to": to_curr,
            "original_amount": str(amount),
            "converted_amount": str(amount_in_to)
        })
