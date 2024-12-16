from datetime import timedelta

from django.utils.timezone import localtime
from rest_framework.exceptions import ParseError
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

    def get_queryset(self):
        # Allow optional filtering by past number of days (via ?days=#).
        qs = super().get_queryset()
        days = self.request.query_params.get("days")
        if days:
            try:
                days = int(days)
                dt_ago = localtime().date() - timedelta(days=days)
            except (TypeError, ValueError):
                raise ParseError("Invalid number of days supplied!")
            qs = qs.filter(date__gte=dt_ago)
        return qs

