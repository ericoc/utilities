from .base import BaseView


class IndexView(BaseView):
    """Index page view."""
    template_name = "index.html"
    title = "Utilities"
