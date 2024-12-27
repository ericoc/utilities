from apps.core.views import BaseView


class WaterView(BaseView):
    """Water usage view."""
    color = "2caffe"
    thresholds = (100, 75, 50)
    time_format = "DataTable.render.date('DDDD')"
    title = "Water"
