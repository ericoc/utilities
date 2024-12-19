from django.db import models
from django.utils.translation import gettext_lazy as _


class ElectricUsage(models.Model):
    """Electric usage table."""

    hour = models.DateTimeField(
        primary_key=True,
        help_text="Start of an hour of electricity usage.",
        verbose_name="Hour"
    )
    kwh = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        help_text=_(
            "Amount of electricity used, in kilowatt-hours (kWh), in an hour."
        ),
        verbose_name="Kilowatt-Hours (kWh)",
    )

    class Meta:
        managed = True
        db_table = "electric"
        ordering = ("hour",)
        verbose_name = _("hour")
        verbose_name_plural = _("hours")
