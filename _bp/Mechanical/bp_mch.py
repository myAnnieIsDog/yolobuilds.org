from django.db import models

from .bp import BP
from .record_types import Type


class Mechanical(BP):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    equipment_units = models.PositiveIntegerField(default=1)
    hvac_units = models.PositiveIntegerField(default=1)
    hvac_type = models.CharField(max_length=255, default="Split")
    hvac_capacity = models.PositiveIntegerField(default=2)
    length_of_ductwork = models.PositiveIntegerField(default=0)
    process_piping = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.number}-Mch"
    
    def add_notes(self):
        if self.wh_type or self.wh_capacity:
            self.notes.append("At inspection provide the CF2R, CF3R and the manufacturer's installation instructions.")

    class Meta:
        ordering = ["number"]
        verbose_name = "Mechanical Permits"
        verbose_name_plural = "Mechanical Permits"
