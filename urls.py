"""URL configuration."""
from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.core.api.routers import api_router
from apps.core.views.error import *


urlpatterns = [
    path("", include("apps.core.urls"), name="core"),
    path("admin/", admin.site.urls, name="admin"),
    path("api/", include(api_router.urls), name="api"),
    path("i18n/", include("django.conf.urls.i18n"), name="i18n"),
]

# Include URLs for apps named starting with "apps." which have models.
for app in apps.get_app_configs():
    if app.models_module and app.name.startswith("apps."):
        urlpatterns.append(
            path(f"{app.label}/", include(f"{app.name}.urls"), name=app.label)
        )

if settings.DEBUG:
    urlpatterns += \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += path("400/", handler400, name="400"),
    urlpatterns += path("401/", handler401, name="401"),
    urlpatterns += path("403/", handler403, name="403"),
    urlpatterns += path("404/", handler404, name="404"),
    urlpatterns += path("405/", handler405, name="405"),
    urlpatterns += path("410/", handler410, name="410"),
    urlpatterns += path("420/", handler420, name="420"),
    urlpatterns += path("500/", handler500, name="500"),
    urlpatterns += path("501/", handler501, name="501"),
    urlpatterns += path("503/", handler503, name="503"),
