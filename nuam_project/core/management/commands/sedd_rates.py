from django.core.management.base import BaseCommand
from core.models import ExchangeRate, Currency

class Command(BaseCommand):
    help = 'Seed exchange rates (example, static)'

    def handle(self, *args, **options):
        rates = {
            'USD': '1.0',  # 1 USD = 1.0 USD
            'CLP': '0.0011',  # 1 CLP = 0.0011 USD -> ejemplo
            'COP': '0.00025', # 1 COP = 0.00025 USD
            'PEN': '0.26',    # 1 PEN = 0.26 USD
        }
        for curr, val in rates.items():
            ExchangeRate.objects.update_or_create(currency=curr, defaults={'rate_to_usd': val})
        self.stdout.write(self.style.SUCCESS('Seeded rates'))
