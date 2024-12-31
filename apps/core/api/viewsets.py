from dateutil.relativedelta import relativedelta

from django.utils.decorators import method_decorator
from django.utils.timezone import localtime
from django.views.decorators.cache import cache_page

from rest_framework.exceptions import ParseError
from rest_framework.viewsets import ReadOnlyModelViewSet


class APIUtilityViewSet(ReadOnlyModelViewSet):
    """Base read-only Django-Rest-Framework (DRF) utility usage API view-set."""
    fields = filterset_fields = "__all__"
    filterable = ("hours", "days", "weeks", "months", "years")
    model = None
    serializer_class = None

    @method_decorator(cache_page(60*2))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()

        if self.filterable:
            for filterable in self.filterable:
                value = self.request.query_params.get(filterable)
                if value:
                    try:
                        # Pass keyword argument to relativedelta() method.
                        ago = {filterable: int(value)}
                        return qs.filter(
                            pk__gte=localtime() - relativedelta(**ago)
                        )
                    except ValueError:
                        raise ParseError(f"Invalid number of {filterable}!")

        return qs
