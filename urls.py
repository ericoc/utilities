"""URL configuration."""
from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.core.api.routers import api_router


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
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
