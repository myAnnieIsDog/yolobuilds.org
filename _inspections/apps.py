from django.apps import AppConfig


class InspectionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "_inspections"
    verbose_name = "Inspection"
    verbose_name_plural = "Inspections"
