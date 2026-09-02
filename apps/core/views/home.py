from django.contrib import messages

from .base import BaseView


class HomeView(BaseView):
    """Home page view."""
    color = "var(--bs-primary)"
    template_name = "base.html"
    title = "Home"

    def setup(self, request, *args, **kwargs):
        # Add welcome message.
        messages.info(request, "Please choose a utility.")
        return super().setup(request, *args, **kwargs)
