from django.contrib.auth.models import User
from django.db import models


class InspectionGroup(models.Model):
    group = models.CharField(max_length=55, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.group

    class Meta:
        ordering = ["group"]
        verbose_name = "Inspection Group"
        verbose_name_plural = "Inspection Groups"


class InspectionType(models.Model):
    name = models.CharField(max_length=255)
    group = models.CharField(max_length=255, default="unassigned")
    group_link = models.ForeignKey(
        InspectionGroup,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="types",
    )
    inspector = models.CharField(max_length=255, default="unassigned")
    hours = models.DecimalField(max_digits=3, decimal_places=1, default=0.3)
    trips = models.DecimalField(max_digits=7, decimal_places=2, default=1.20)
    checklist = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["group", "name"]
        verbose_name = "Inspection Type"
        verbose_name_plural = "Inspection Types"


class InspectionStatus(models.Model):
    status = models.CharField(max_length=55, unique=True)
    description = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.status

    class Meta:
        ordering = ["status"]
        verbose_name = "Inspection Result Option"
        verbose_name_plural = "Inspection Result Options"


class TripResult(models.Model):
    result = models.CharField(max_length=55, unique=True)
    description = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.result

    class Meta:
        ordering = ["result"]
        verbose_name = "Inspection Trip Result Option"
        verbose_name_plural = "Inspection Trip Result Options"


class Inspection(models.Model):
    record = models.CharField(max_length=55)
    type = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True)

    time_allotted = models.DecimalField(max_digits=7, decimal_places=1)
    time_actual = models.DecimalField(max_digits=7, decimal_places=1)
    time_delta = models.DecimalField(max_digits=7, decimal_places=1)

    def __str__(self) -> str:
        return self.type

    class Meta:
        ordering = ["type"]
        verbose_name = "Inspection"
        verbose_name_plural = "Inspections"


class InspectionTrip(models.Model):
    inspection = models.CharField(max_length=55)
    inspection_link = models.ForeignKey(
        Inspection, on_delete=models.PROTECT, related_name="trips"
    )
    trip_number = models.PositiveSmallIntegerField(default=0)
    result = models.CharField(max_length=55, unique=True)
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
