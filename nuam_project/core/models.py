from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Location(models.TextChoices):
    CHILE = 'CL', 'Chile'
    COLOMBIA = 'CO', 'Colombia'
    PERU = 'PE', 'Perú'
    USA = 'US', 'Estados Unidos'

class Currency(models.TextChoices):
    CLP = 'CLP', 'Peso chileno'
    COP = 'COP', 'Peso colombiano'
    PEN = 'PEN', 'Sol peruano'
    USD = 'USD', 'Dólar estadounidense'

class ExchangeRate(models.Model):
    currency = models.CharField(max_length=3, choices=Currency.choices, unique=True)
    rate_to_usd = models.DecimalField(max_digits=20, decimal_places=8)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.currency} -> {self.rate_to_usd} USD"

class Transaction(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=14, decimal_places=2, validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=3, choices=Currency.choices)
    location = models.CharField(max_length=2, choices=Location.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def amount_in_usd(self):
        try:
            rate = ExchangeRate.objects.get(currency=self.currency)
            return (self.amount * rate.rate_to_usd).quantize(Decimal('0.01'))
        except ExchangeRate.DoesNotExist:
            return None
