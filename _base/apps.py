from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "_base"
    verbose_name = "Base Module"
    verbose_name_plural = "Base Module"
