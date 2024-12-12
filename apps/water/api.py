from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import WaterUsage


class WaterUsageSerializer(ModelSerializer):
    """Django-Rest-Framework (DRF) serializer for water usage API endpoint."""
    class Meta:
        model = WaterUsage
        fields = "__all__"


class APIWaterUsageViewSet(ReadOnlyModelViewSet):
    """Water usage in gallons per day."""
    fields = filterset_fields = "__all__"
    model = WaterUsage
    queryset = model.objects
    serializer_class = WaterUsageSerializer
