from datetime import timedelta

from django.utils.timezone import localtime
from rest_framework.exceptions import ParseError
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

    def get_queryset(self):
        # Allow optional filtering by past number of days (via ?days=#).
        qs = super().get_queryset()
        days = self.request.query_params.get("days")
        if days:
            try:
                days = int(days)
                dt_ago = localtime() - timedelta(days=days)
            except (TypeError, ValueError):
                raise ParseError("Invalid number of days supplied!")
            qs = qs.filter(hour__gte=dt_ago)
        return qs
