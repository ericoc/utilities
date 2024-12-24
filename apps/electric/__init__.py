from django.apps import AppConfig


class ElectricConfig(AppConfig):
    app_label = "electric"
    default_auto_field = "django.db.models.DateTimeField"
    name = "apps.electric"
    verbose_name = "Electric"
    verbose_name_plural = "Electric"
