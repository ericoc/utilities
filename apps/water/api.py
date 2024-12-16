from datetime import timedelta

from django.utils.timezone import localdate
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
    no_filter = ("hours", "months")
    queryset = model.objects
    serializer_class = WaterUsageSerializer

    def get_queryset(self):
        # Allow optional filtering by past number of days (via ?days=#).
        qs = super().get_queryset()

        for not_filterable in self.no_filter:
            if self.request.query_params.get(not_filterable):
                raise ParseError(f"Invalid parameter: {not_filterable}!")

        try:
            days = self.request.query_params.get("days")
            if days:
                return qs.filter(
                    pk__gte=localdate() - timedelta(days=int(days))
                )
        except ValueError:
            raise ParseError("Invalid number of days!")

        return qs
