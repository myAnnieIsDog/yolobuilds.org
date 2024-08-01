from django.db import models

from .bp import  BP
from .record_types import Type


class Grading(BP):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    purpose = models.CharField(max_length=20, null=True)
    disturbed_area = models.PositiveIntegerField(default=1000)
    max_cut_depth = models.PositiveIntegerField(default=3)
    max_cut_slope = models.PositiveIntegerField(default=3)
    max_fill_height = models.PositiveIntegerField(default=3)
    max_fill_slope = models.PositiveIntegerField(default=3)
    geotech_report = models.BooleanField(default=True)
    special_inspection = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.number}-Grd"
    
    class Meta:
        ordering = ["number"]
        verbose_name = "Grading Permits"
        verbose_name_plural = "Grading Permits"
