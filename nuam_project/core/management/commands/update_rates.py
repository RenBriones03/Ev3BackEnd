from django.core.management.base import BaseCommand
from core.models import ExchangeRate
import requests
import math

class Command(BaseCommand):
    help = "Actualiza las tasas de cambio (CLP, COP, PEN, USD) desde open.er-api.com"

    def handle(self, *args, **kwargs):
        self.stdout.write("🔄 Actualizando tasas de cambio...")

        try:
            url = "https://open.er-api.com/v6/latest/USD"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            if "rates" not in data or not isinstance(data["rates"], dict):
                self.stderr.write(f"❌ Respuesta inesperada de la API: {data}")
                return

            rates = data["rates"]

            for c in ["USD", "CLP", "COP", "PEN"]:
                if c not in rates:
                    self.stderr.write(f"⚠️ Falta tasa para {c} en la respuesta.")
                    return

            # USD = 1 siempre
            ExchangeRate.objects.update_or_create(currency="USD", defaults={"rate_to_usd": 1})

            # Las demás monedas (1 USD = rate moneda)
            for c in ["CLP", "COP", "PEN"]:
                rate = rates[c]
                if rate != 0:
                    rounded_rate = math.floor(rate)  # Redondea hacia abajo a número entero
                    ExchangeRate.objects.update_or_create(
                        currency=c, defaults={"rate_to_usd": 1 / rounded_rate}
                    )

            self.stdout.write("✅ Tasas actualizadas correctamente:")
            for c in ["CLP", "COP", "PEN"]:
                self.stdout.write(f"   1 USD = {math.floor(rates[c])} {c}")

        except Exception as e:
            self.stderr.write(f"⚠️ Error al actualizar las tasas: {e}")
