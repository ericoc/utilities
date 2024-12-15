from rest_framework.routers import DefaultRouter

from apps.electric.api import APIElectricUsageViewSet
from apps.gas.api import APIGasUsageViewSet
from apps.water.api import APIWaterUsageViewSet


api_router = DefaultRouter()

api_router.register(prefix=r"electric", viewset=APIElectricUsageViewSet)
api_router.register(prefix=r"gas", viewset=APIGasUsageViewSet)
api_router.register(prefix=r"water", viewset=APIWaterUsageViewSet)
