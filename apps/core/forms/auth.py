from django.contrib.auth.views import LoginView, LogoutView

from ..views.base import BaseView


class UtilitiesLoginView(BaseView, LoginView):
    """Log in view."""
    success_url = '/add/'
    template_name = "login.html"
    title = "Log in"


class UtilitiesLogoutView(BaseView, LogoutView):
    """Log out view."""
    template_name = "login.html"
    title = "Log out"
