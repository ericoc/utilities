from django.contrib import admin
from django.urls import include, path

from .views import IndexView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("admin/", admin.site.urls, name="admin"),
    path("i18n/", include('django.conf.urls.i18n')),
]
