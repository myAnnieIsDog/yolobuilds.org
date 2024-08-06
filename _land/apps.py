from django.apps import AppConfig


class LandConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "_land"
    verbose_name = "Parcel / Address"
    verbose_name_plural = "Parcels and Addresses"
