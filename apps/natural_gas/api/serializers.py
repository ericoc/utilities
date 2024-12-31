from apps.core.api.serializers import APIUtilitySerializer

from ..models import NaturalGasUsage


class NaturalGasUsageSerializer(APIUtilitySerializer):
    """Django-Rest-Framework (DRF) serializer for natural gas usage."""
    class Meta:
        model = NaturalGasUsage
        fields = "__all__"
