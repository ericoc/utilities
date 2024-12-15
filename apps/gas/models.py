from django.db import models
from django.utils.translation import gettext_lazy as _


class GasUsage(models.Model):
    """Natural gas usage table."""

    month = models.DateField(
        primary_key=True,
        help_text=_("Billing month of natural gas usage."),
        verbose_name=_("Month")
    )
    ccf = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text=_(
            "Amount of natural gas used,"
            " in hundreds of cubic feet (CCF), in a month."
        ),
        verbose_name=_("Hundreds of Cubic Feet (CCF)"),
    )

    class Meta:
        managed = True
        db_table = "gas"
        ordering = ("month",)
        verbose_name = verbose_name_plural = _("Natural Gas Usage")
