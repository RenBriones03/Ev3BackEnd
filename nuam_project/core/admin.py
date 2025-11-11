from django.contrib import admin
from .models import Transaction, ExchangeRate

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id','description','amount','currency','location','created_at')
    list_filter = ('currency','location')
    search_fields = ('description',)

@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('currency','rate_to_usd','updated_at')
