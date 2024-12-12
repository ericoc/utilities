"""isharmud.com root URL configuration."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from api import api_router


urlpatterns = [
    path("", include("apps.core.urls"), name="core"),
    path("electric/", include("apps.electric.urls"), name="electric"),
    path("water/", include("apps.water.urls"), name="water"),
    path("admin/", admin.site.urls, name="admin"),
    path("api/", include(api_router.urls), name="api"),
    path("i18n/", include('django.conf.urls.i18n'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
