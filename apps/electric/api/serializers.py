from apps.core.api.serializers import APIUtilitySerializer

from ..models import ElectricUsage


class ElectricUsageSerializer(APIUtilitySerializer):
    """Django-Rest-Framework (DRF) serializer for electric usage."""
    class Meta:
        model = ElectricUsage
        fields = "__all__"
