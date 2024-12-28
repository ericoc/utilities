from django.db import models
from django.utils.translation import gettext_lazy as _


class WaterUsage(models.Model):
    """Water usage table."""
    day = models.DateField(
        primary_key=True,
        help_text=_("Date of water usage."),
        verbose_name=_("Day")
    )
    gallons = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        help_text=_("Amount of water usage in gallons, on the day."),
        verbose_name=_("Gallons")
    )

    class Meta:
        managed = True
        db_table = "water"
        ordering = ("day",)
        verbose_name = _("day")
        verbose_name_plural = _("days")
