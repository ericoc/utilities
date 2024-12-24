from django.apps import AppConfig


class GasConfig(AppConfig):
    app_label = "gas"
    default_auto_field = "django.db.models.DateField"
    name = "apps.gas"
    verbose_name = "(Natural) Gas"
    verbose_name_plural = "(Natural) Gas"
