from django.db import models

from .fee_types import FeeType
from .inspection_types import InspectionType
from .review_types import ReviewType
from .profile_staff import Division


class Type(models.Model): 
    division = models.ForeignKey(Division, on_delete=models.PROTECT, blank=True, null=True)
    prefix = models.CharField(max_length=7, blank=True, null=True)
    type = models.CharField(max_length=55, blank=True, null=True)
    policy = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=7, blank=True, null=True)
    default_fees = models.ManyToManyField(FeeType, blank=True)
    default_reviews = models.ManyToManyField(ReviewType, blank=True)
    default_inspection = models.ManyToManyField(InspectionType, blank=True)

    def __str__(self) -> str:
        return self.type
    
    class Meta():
        ordering = ["type"]
        verbose_name = "Type"
        verbose_name_plural = "Types"
