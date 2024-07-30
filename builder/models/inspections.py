from django.db import models

from .bp import BP
from .inspection_types import InspectionType


class InspectionStatus(models.Model): 
    status = models.CharField(max_length=55, unique=True)
    active = models.BooleanField(default=True) # set to False instead of deleting if a status will no longer be used. 

    def __str__(self) -> str:
        return self.status

    class Meta():
        ordering = ["status"]
        verbose_name = "Inspection Status Option"
        verbose_name_plural = "Inspection Status Options"


class Inspection(models.Model):
    record = models.ForeignKey(BP, on_delete=models.DO_NOTHING, null=True, blank = True, related_name = "inspection")
    type = models.ForeignKey(InspectionType, on_delete=models.PROTECT, related_name = "inspection")   
    status = models.ForeignKey(InspectionStatus, on_delete=models.PROTECT) 

    """ Fee Study """
    staff_time_allotted = models.DecimalField(max_digits=7, decimal_places=1)
    staff_time_actual = models.DecimalField(max_digits=7, decimal_places=1)     

    def __str__(self) -> str:
        return self.type
    
    class Meta():
        ordering = ["type"]
        verbose_name = "Inspection"
        verbose_name_plural = "Inspections"

class TripResult(models.Model):
    pass

class InspectionTrip(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.PROTECT, related_name = "trip")  
    trip_number = models.PositiveSmallIntegerField(default=0) 
    result = models.ForeignKey(TripResult, on_delete=models.PROTECT)   
    resulted = models.DateTimeField(null=True)
    inspector = models.CharField(max_length=100, null=True, blank=True)

    time_allotted = models.DecimalField(max_digits=7, decimal_places=1)
    time_actual = models.DecimalField(max_digits=7, decimal_places=1)
    time_delta = models.DecimalField(max_digits=7, decimal_places=1)

    scheduled_date = models.DateField()
    scheduled_time = models.TimeField()

    requested_by = models.CharField(max_length=100, null=True, blank=True)
    requested_date = models.DateField()
    requested_notes = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        ordering = ["inspection", "trip_number"]
        verbose_name = "Inspection Trip"
        verbose_name_plural = "Inspection Trips"
