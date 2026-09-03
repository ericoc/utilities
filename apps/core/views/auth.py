from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView

from .base import BaseView


class UtilitiesLoginView(LoginView, BaseView, FormView):
    """Log in view."""
    color = "var(--bs-success)"
    http_method_names = ("get", "post")
    success_url = "/add/"
    template_name = "login.html"
    title = "Log in"

    def get_success_url(self):
        # Add message upon successful log in.
        messages.success(self.request, "You have been logged in.")
        return super().get_success_url()

class UtilitiesLogoutView(LogoutView):
    """Log out view."""
    template_name = "login.html"
    title = "Log in"

    def get_success_url(self):
        # Add message upon successful log out.
        messages.success(self.request, "You have been logged out.")
        return super().get_success_url()
