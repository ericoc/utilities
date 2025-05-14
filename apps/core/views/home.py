from .base import BaseView


class HomeView(BaseView):
    """Home page view."""
    color = "var(--bs-primary)"
    template_name = "home.html"
    title = "Home"
