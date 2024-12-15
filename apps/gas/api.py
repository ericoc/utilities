from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import GasUsage


class GasUsageSerializer(ModelSerializer):
    """Django-Rest-Framework (DRF) serializer for natural gas usage."""
    class Meta:
        model = GasUsage
        fields = "__all__"


class APIGasUsageViewSet(ReadOnlyModelViewSet):
    """Natural gas usage API view."""
    fields = filterset_fields = "__all__"
    model = GasUsage
    queryset = model.objects
    serializer_class = GasUsageSerializer
