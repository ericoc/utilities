from apps.core.api.viewsets import APIUtilityViewSet

from .serializers import WaterUsageSerializer

from ..models import WaterUsage


class APIWaterUsageViewSet(APIUtilityViewSet):
    """Django-Rest-Framework (DRF) water usage API view-set."""
    model = WaterUsage
    queryset = model.objects
    filterable = ("hours", "months")
    serializer_class = WaterUsageSerializer
