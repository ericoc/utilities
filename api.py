from rest_framework.routers import DefaultRouter

from apps.electric.api import APIElectricUsageViewSet
from apps.water.api import APIWaterUsageViewSet


api_router = DefaultRouter()

api_router.register(prefix=r"electric", viewset=APIElectricUsageViewSet)
api_router.register(prefix=r"water", viewset=APIWaterUsageViewSet)
