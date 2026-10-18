from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ReadOnlyModelViewSet


class APIUtilityViewSet(ReadOnlyModelViewSet):
    """
    Base read-only Django-Rest-Framework (DRF) utility usage API view-set.
    """
    filter_backends = (OrderingFilter,)
    filterset_fields = fields = ordering_fields = "__all__"
