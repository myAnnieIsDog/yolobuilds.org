from django.db import models

from .profiles import Profile


class Agency(models.Model):
    agency = models.CharField(max_length=25, unique=True)
    full_agency = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.agency
    
    class Meta:
        ordering = ["agency"]
        verbose_name = "Yolo DCS Partner Agency"
        verbose_name_plural = "Yolo DCS Partner Agencies"


class YoloCountyPartners(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.PROTECT)
    agency = models.ForeignKey(
        Agency, on_delete=models.PROTECT)
    alt_contact_name = models.CharField(max_length=255, null=True, blank=True)
    alt_contact_email = models.CharField(max_length=255, null=True, blank=True)
    # recent_records = models.ManyToManyField(Record)

    def __str__(self) -> str:
        return self.profile.user.username
    
    class Meta():
        ordering = ["agency", "profile"]
        verbose_name = "Yolo DCS Partner"
        verbose_name_plural = "Yolo DCS Partners"
