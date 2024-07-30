from django.db import models

from .bp import BP
from .record_types import Type
from .locations import FloodZones


class Flood(BP):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    zone = models.ForeignKey(FloodZones, on_delete=models.PROTECT)
    bfe = models.PositiveIntegerField(null=True)
    design_depth = models.PositiveIntegerField(null=True)

    FEMA_defined_structure = models.BooleanField(null=True)
    substantial_improvement = models.BooleanField(null=True)
    variance = models.BooleanField(null=True)

    def __str__(self) -> str:
        return f"{self.number}-Fld"

    class Meta:
        # ordering = ["number"]
        verbose_name = "Flood Protection Permits"
        verbose_name_plural = "Flood Protection Permits"
