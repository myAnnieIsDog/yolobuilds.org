from django.db import models

from .bp import BP
from .record_types import Type


class Fire(BP):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    suffix = "Fire"
    sprinkler_heads = models.PositiveIntegerField(default=20)
    sprinkler_area = models.PositiveIntegerField(default=2000)

    new_alarm_system = models.BooleanField(False)
    fire_detectors = models.PositiveIntegerField(default=20)

    hazardous_material = models.BooleanField(False)
    high_piled_combustible_storage = models.BooleanField(False)

    def __str__(self) -> str:
        return f"{self.number}-Fire"
    
    class Meta:
        ordering = ["number"]
        verbose_name = "Fire Protection Permits"
        verbose_name_plural = "Fire Protection Permits"
