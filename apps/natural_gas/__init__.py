from django.apps import AppConfig


class NaturalGasConfig(AppConfig):
    app_label = "natural_gas"
    default_auto_field = "django.db.models.DateField"
    name = "apps.natural_gas"
    verbose_name = verbose_name_plural = "Natural Gas"
