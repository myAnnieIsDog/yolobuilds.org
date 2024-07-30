from django.db import models

from .bp import BP
from .record_types import Type


class Pool(BP):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    public = models.BooleanField(default=False)
    area = models.PositiveIntegerField("Area (square feet)", blank=True)
    depth = models.PositiveIntegerField("Depth (feet)", blank=True)

    enclosure = models.BooleanField(default=False)
    structural = models.BooleanField(default=False)
    accessibility = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.number}-Pool"
    
    class Meta:
        ordering = ["number"]
        verbose_name = "Pool/Spa Permits"
        verbose_name_plural = "Pool/Spa Permits"
