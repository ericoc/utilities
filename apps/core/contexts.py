"""Define contexts from Django settings."""
from django.conf import settings


def contexts(request):
    """Contexts."""
    items = {"TIME_ZONE": None, "UTILITIES": None, "WEBSITE_TITLE": None}
    for item in items:
        items[item] = settings.__getattr__(item) or None
    return items
