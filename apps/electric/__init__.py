from django.apps import AppConfig


class ElectricConfig(AppConfig):
    app_label = "electric"
    color: "e4a11b"
    default_auto_field = "django.db.models.DateTimeField"
    icon = "lightbulb"
    name = "apps.electric"
    verbose_name = "Electric"
    verbose_name_plural = "Electric"
