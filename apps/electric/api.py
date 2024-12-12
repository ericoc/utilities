from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import ElectricUsage


class ElectricUsageSerializer(ModelSerializer):
    """Django-Rest-Framework (DRF) serializer for electric usage."""
    class Meta:
        model = ElectricUsage
        fields = "__all__"


class APIElectricUsageViewSet(ReadOnlyModelViewSet):
    """Electric usage API view."""
    fields = filterset_fields = "__all__"
    model = ElectricUsage
    queryset = model.objects
    serializer_class = ElectricUsageSerializer
