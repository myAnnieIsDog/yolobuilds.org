from django.contrib.auth.models import User
from django.db import models


class InspectionGroup(models.Model):
    group = models.CharField(max_length=55, blank=True)

    def __str__(self) -> str:
        return self.group

    class Meta():
        ordering = ["group"]
        verbose_name = "Inspection Group"
        verbose_name_plural = "Inspection Groups"


class InspectionType(models.Model): 
    inspection_type = models.CharField(max_length=255)
    insp_group = models.ForeignKey(InspectionGroup, on_delete=models.PROTECT, null=True, blank=True)
    default_inspector = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    duration_hours = models.DecimalField(max_digits=3, decimal_places=1, default=0.3)
    trip_factor = models.DecimalField(max_digits=7, decimal_places=2, default=1.20)
    inspection_checklist = models.TextField(blank=True)

    
    def __str__(self) -> str:
        return self.inspection_type

    class Meta():
        ordering = ["insp_group", "inspection_type"]
        verbose_name = "Inspection Type"
        verbose_name_plural = "Inspection Types"
