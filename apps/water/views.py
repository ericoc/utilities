from apps.core.views import UtilityView

from .models import WaterUsage


class WaterView(UtilityView):
    """Water usage view."""
    color = "2caffe"
    datatable_time_format = "date('DDDD')"
    model = WaterUsage
    thresholds = (100, 75, 50)
    title = "Water"
