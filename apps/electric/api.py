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
        # Allow optional filtering by past number of hours or days.
        qs = super().get_queryset()
        ago = None

        filterables = ("days", "hours")
        for filterable in filterables:
            value = self.request.query_params.get(filterable)

            if value:
                try:
                    num_value = int(value)
                    if filterable == 'days':
                        ago = timedelta(days=num_value)
                    elif filterable == 'hours':
                        ago = timedelta(hours=num_value)
                except (TypeError, ValueError):
                    raise ParseError(f"Invalid ${filterable} value supplied!")

                if ago:
                    dt_ago = localtime() - ago
                    return qs.filter(hour__gte=dt_ago)
        return qs
