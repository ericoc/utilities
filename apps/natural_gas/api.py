from dateutil.relativedelta import relativedelta

from django.utils.timezone import localdate
from rest_framework.exceptions import ParseError
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import NaturalGasUsage


class NaturalGasUsageSerializer(ModelSerializer):
    """Django-Rest-Framework (DRF) serializer for natural gas usage."""
    class Meta:
        model = NaturalGasUsage
        fields = "__all__"


class APINaturalGasUsageViewSet(ReadOnlyModelViewSet):
    """Natural gas usage API view."""
    fields = filterset_fields = "__all__"
    model = NaturalGasUsage
    no_filter = ("days", "hours")
    queryset = model.objects
    serializer_class = NaturalGasUsageSerializer

    def get_queryset(self):
        # Allow optional filtering by past number of months (via ?months=#).
        qs = super().get_queryset()

        for not_filterable in self.no_filter:
            if self.request.query_params.get(not_filterable):
                raise ParseError(f"Invalid parameter: {not_filterable}!")

        try:
            months = self.request.query_params.get("months")
            if months:
                return qs.filter(
                    pk__gte=localdate() - relativedelta(months=int(months))
                )
        except (TypeError, ValueError):
            raise ParseError("Invalid number of months!")
        return qs
