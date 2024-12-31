from apps.core.api.viewsets import APIUtilityViewSet

from .serializers import NaturalGasUsageSerializer

from ..models import NaturalGasUsage


class APINaturalGasUsageViewSet(APIUtilityViewSet):
    """Django-Rest-Framework (DRF) natural gas usage API view-set."""
    model = NaturalGasUsage
    queryset = model.objects
    filterable = ("months", "years")
    serializer_class = NaturalGasUsageSerializer
