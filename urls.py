"""isharmud.com root URL configuration."""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from api import api_router

urlpatterns = [
    path("", include("apps.core.urls"), name="core"),
    path("api/", include(api_router.urls), name="api"),
    path("electric/", include("apps.electric.urls"), name="electric"),
    path("gas/", include("apps.gas.urls"), name="gas"),
    path("water/", include("apps.water.urls"), name="water"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
