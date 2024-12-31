from .base import BaseView


class HomeView(BaseView):
    """Home page view."""
    template_name = "home.html"
    title = "Home"
