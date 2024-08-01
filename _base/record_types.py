from django.db import models

from _fiscal.models import FeeType
from _base.inspection_types import InspectionType
from _base.review_types import ReviewType
from _profiles.profile_staff import Division


class Type(models.Model):
    division = models.ForeignKey(
        Division, on_delete=models.PROTECT, blank=True, null=True
    )
    prefix = models.CharField(max_length=7, blank=True, null=True)
    type = models.CharField(max_length=55, blank=True, null=True)
    policy = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=7, blank=True, null=True)
    default_fees = models.ManyToManyField(FeeType, blank=True)
    default_reviews = models.ManyToManyField(ReviewType, blank=True)
    default_inspection = models.ManyToManyField(InspectionType, blank=True)

    def __str__(self) -> str:
        return self.type

    class Meta:
        ordering = ["type"]
        verbose_name = "Record Type"
        verbose_name_plural = "Record Types"
