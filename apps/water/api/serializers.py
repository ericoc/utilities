from apps.core.api.serializers import APIUtilitySerializer

from ..models import WaterUsage


class WaterUsageSerializer(APIUtilitySerializer):
    """Django-Rest-Framework (DRF) serializer for water usage."""
    class Meta:
        model = WaterUsage
        fields = "__all__"
