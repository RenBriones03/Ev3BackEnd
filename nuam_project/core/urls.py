from rest_framework import routers
from .views import TransactionViewSet, ExchangeRateViewSet

router = routers.DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'exchange-rates', ExchangeRateViewSet, basename='exchange-rates')

urlpatterns = router.urls
