from apps.core.api.viewsets import APIUtilityViewSet

from .serializers import ElectricUsageSerializer

from ..models import ElectricUsage


class APIElectricUsageViewSet(APIUtilityViewSet):
    """Django-Rest-Framework (DRF) natural gas usage API view-set."""
    model = ElectricUsage
    queryset = model.objects
    filterable = ("months", "years")
    serializer_class = ElectricUsageSerializer
