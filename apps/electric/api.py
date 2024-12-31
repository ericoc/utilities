from apps.core.api import APIUtilitySerializer, APIUtilityViewSet

from .models import ElectricUsage


class ElectricUsageSerializer(APIUtilitySerializer):
    """Django-Rest-Framework (DRF) serializer for electric usage."""
    class Meta:
        model = ElectricUsage


class ElectricUsageViewSet(APIUtilityViewSet):
    """Django-Rest-Framework (DRF) electric usage API view-set."""
    model = ElectricUsage
    serializer_class = ElectricUsageSerializer
    filterable = ("hours", "days", "weeks", "months", "years")
