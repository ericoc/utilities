from django.apps import AppConfig


class WaterConfig(AppConfig):
    app_label = "water"
    color: "2caffe"
    default_auto_field = "django.db.models.DateField"
    icon = "droplet"
    name = "apps.water"
    verbose_name = "Water"
    verbose_name_plural = "Water"
