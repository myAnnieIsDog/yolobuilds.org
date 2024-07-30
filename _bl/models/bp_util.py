from django.db import models

from .bp import BP
from .record_types import Type


class Utility(BP):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    accessory_utility_new_area = models.PositiveIntegerField(default=0)
    residential_dwelling_new_units = models.PositiveIntegerField(default=0)
    residential_dwelling_new_area = models.PositiveIntegerField(default=0)
    assembly_new_area = models.PositiveIntegerField(default=0)
    office_new_area = models.PositiveIntegerField(default=0)
    processing_or_production_new_area = models.PositiveIntegerField(default=0)
    warehouse_new_area = models.PositiveIntegerField(default=0)
    retail_new_area = models.PositiveIntegerField(default=0)
    other_new_area = models.PositiveIntegerField(default=0)
    other_description = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.number}-NewU"
    
    class Meta:
        verbose_name = "New Accessory/Utility Structure"
        verbose_name_plural = "New Accessory/Utility Structures"
