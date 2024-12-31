from django.apps import AppConfig


class WaterConfig(AppConfig):
    app_label = "water"
    default_auto_field = "django.db.models.DateField"
    name = "apps.water"
    verbose_name = verbose_name_plural = "Water"
