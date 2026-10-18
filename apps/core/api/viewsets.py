from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ReadOnlyModelViewSet


class APIUtilityViewSet(ReadOnlyModelViewSet):
    """
    Base read-only Django-Rest-Framework (DRF) utility usage API view-set.
    """
    fields = "__all__"
    filter_backends = (OrderingFilter,)
    ordering_fields = "__all__"
