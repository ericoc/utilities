from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.forms import ValidationError
from django.utils.html import format_html
from django.utils.translation import ngettext
from django.views.generic.edit import FormView

from apps.electric.models import ElectricUsage
from apps.natural_gas.models import NaturalGasUsage
from apps.water.models import WaterUsage

from .base import BaseView
from ..forms import UploadUsageDataForm


class AddView(LoginRequiredMixin, BaseView, FormView):
    """Add data via upload form view."""
    color = "var(--bs-success)"
    form_class = UploadUsageDataForm
    http_method_names = ("get", "post")
    model = None
    success_url = "/add/"
    template_name = "add.html"
    title = "Add"

    def form_valid(self, form):

        model = None
        num_created = 0
        utility = form.cleaned_data.get("utility")
        if not utility:
            raise ValidationError("Missing utility!")

        # Choose model uniquely per utility.
        if utility == "electric":
            model = ElectricUsage
        if utility == "natural_gas":
            model = NaturalGasUsage
        if utility == "water":
            model = WaterUsage

        # Ensure that a model is chosen.
        if not model:
            raise ValidationError(f"Missing model (for {utility})!")

        # Ensure that data was found from the uploaded utility usage file.
        usage = form.cleaned_data.get("usage")
        if not usage:
            raise ValidationError(f"Missing usage (for {utility}!")

        # Count the number of usage records found in the uploaded file.
        num_found = len(usage)
        utility_title = utility.replace("_", " ")

        # Message the utility that was detected based upon the file.
        messages.add_message(
            request=self.request,
            level=messages.INFO,
            message=format_html(f"<b>Utility</b>: {utility_title.title()}")
        )

        # Message the count of usage events that were found in the file.
        found_msg = ngettext(
            singular=f"%d {model._meta.verbose_name.title()}",
            plural=f"%d {model._meta.verbose_name_plural.title()}",
            number=num_found,
        ) % num_found
        messages.add_message(
            request=self.request,
            level=messages.INFO,
            message=format_html(f"<b>Found</b>: {found_msg}")
        )

        # Add each usage item to database.
        for usage_item in usage:
            obj, created = model.objects.update_or_create(
                **usage_item,
                defaults=usage_item
            )
            if created:
                num_created += 1

        # Message count of usage events that were created from uploaded file.
        create_level = messages.INFO
        if num_created > 0:
            create_level = messages.SUCCESS
        create_msg = ngettext(
            singular=f"%d {model._meta.verbose_name.title()}",
            plural=f"%d {model._meta.verbose_name_plural.title()}",
            number=num_created,
        ) % num_created
        messages.add_message(
            request=self.request,
            level=create_level,
            message=format_html(f"<b>Created</b>: {create_msg}")
        )

        return super().form_valid(form)
