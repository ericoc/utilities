from rest_framework.routers import DefaultRouter

from apps.electric.api.viewsets import APIElectricUsageViewSet
from apps.natural_gas.api.viewsets import APINaturalGasUsageViewSet
from apps.water.api.viewsets import APIWaterUsageViewSet


api_router = DefaultRouter()

api_router.register("electric", APIElectricUsageViewSet)
api_router.register("natural_gas", APINaturalGasUsageViewSet)
api_router.register("water", APIWaterUsageViewSet)
