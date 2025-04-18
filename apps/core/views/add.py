from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

from ..forms.upload import UploadUsageDataForm
from .base import BaseView

class AddView(LoginRequiredMixin, BaseView, FormView):
    """Add data via upload form view."""
    color = "var(--bs-success)"
    form_class = UploadUsageDataForm
    success_url = "/add/"
    template_name = "add.html"
    title = "Add"
