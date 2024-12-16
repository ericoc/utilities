from dateutil.relativedelta import relativedelta

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
        # Allow optional filtering by past number of days, hours, or months.
        qs = super().get_queryset()

        for filterable in ("hours", "days", "months"):
            value = self.request.query_params.get(filterable)
            if value:
                try:
                    # Dictionary of one of the three (3):
                    #   {"hours": value}, {"days": value}, or {"months": value}
                    #   to pass keyword argument to relativedelta() method.
                    ago = {filterable: int(value)}
                    return qs.filter(
                        pk__gte=localtime() - relativedelta(**ago)
                    )
                except ValueError:
                    raise ParseError(f"Invalid number of {filterable}!")

        return qs
