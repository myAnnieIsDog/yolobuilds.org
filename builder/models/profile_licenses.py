from django.db import models

from .profiles import Profile


class LicenseAgency(models.Model):
    agency = models.CharField("Agency Acronym", max_length=15, unique=True)
    agency_long = models.CharField("Agency Full Name", max_length=255, unique=True)

    def __str__(self) -> str:
        return self.agency_long
    
    class Meta:
        ordering = ["agency"]
        verbose_name = "Certification Agency"
        verbose_name_plural = "Certification Agencies"


class LicenseType(models.Model):
    licensing_agency = models.ForeignKey(LicenseAgency, on_delete=models.PROTECT, null=True)
    license_short = models.CharField("Licens Type", max_length=7, unique=True)
    license_long = models.CharField("Licens Type", max_length=255, unique=True)

    def __str__(self) -> str:
        return self.license_long

    class Meta:
        ordering = ["license_short"]
        verbose_name = "Certification Type"
        verbose_name_plural = "Certification Types"


class LicenseHolder(models.Model):
    license_holder = models.ForeignKey(Profile, on_delete=models.PROTECT)
    license_type = models.ForeignKey(LicenseType, on_delete=models.PROTECT)
    license_number = models.CharField(max_length=255, unique=True)
    expiration_date = models.DateField()
    verified_valid = models.BooleanField()
    # replace the following with a relationship to business license records.
    bl_number = models.CharField(
        "Yolo County Business License Number", max_length=40, blank=True)

    def __str__(self) -> str:
        return f"{self.license_holder} {self.license_type}"
    
    class Meta:
        ordering = ["license_holder", "license_type"]
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"