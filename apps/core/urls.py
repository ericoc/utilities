from django.urls import path
from django.views.generic.base import RedirectView

from .views.add import AddView
from .views.home import HomeView
from .views.auth import UtilitiesLoginView, UtilitiesLogoutView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add/", AddView.as_view(), name="add"),
    path("login/", UtilitiesLoginView.as_view(), name="login"),
    path("logout/", UtilitiesLogoutView.as_view(), name="logout"),
    path("favicon.ico", RedirectView.as_view(url="static/favicon.ico"))
]
