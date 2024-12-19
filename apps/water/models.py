from django.db import models
from django.utils.translation import gettext_lazy as _


class WaterUsage(models.Model):
    """Water usage table."""

    date = models.DateField(
        primary_key=True,
        help_text="Date of water usage.",
        verbose_name="Date"
    )
    gallons = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        help_text="Amount of water usage in gallons on the date.",
        verbose_name="Gallons"
    )

    class Meta:
        managed = True
        db_table = "water"
        ordering = ("date",)
        verbose_name = _("day")
        verbose_name_plural = _("days")
