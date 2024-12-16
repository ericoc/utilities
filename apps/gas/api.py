from dateutil.relativedelta import relativedelta

from django.utils.timezone import localdate
from rest_framework.exceptions import ParseError
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

    def get_queryset(self):
        # Allow optional filtering by past number of months (via ?months=#).
        qs = super().get_queryset()
        months = self.request.query_params.get("months")
        if months:
            try:
                months = int(months)
                dt_ago = localdate() - relativedelta(months=months)
            except (TypeError, ValueError):
                raise ParseError("Invalid number of months supplied!")
            qs = qs.filter(month__gte=dt_ago)
        return qs
