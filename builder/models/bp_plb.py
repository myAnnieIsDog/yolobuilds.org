from django.db import models

from .bp import BP
from .record_types import Type


class Plumbing(BP):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    general_fixtures = models.PositiveIntegerField(default=1000)

    water_supply_service = models.PositiveIntegerField(default=100)
    waste_water_service = models.PositiveIntegerField(default=100)

    sewer_diameter = models.PositiveIntegerField(blank=True)
    sewer_material = models.CharField(max_length=55, help_text="ABS")
    sewer_trenchless = models.BooleanField(default=False)

    wh_type = models.CharField(max_length=255, default="Heat Pump")
    wh_capacity = models.PositiveIntegerField(default=50)

    fuel = models.CharField(max_length=55, help_text="Propane")
    fuel_gas_appliance = models.PositiveIntegerField(default=1000)
    fuel_gas_pipe_length = models.PositiveIntegerField(blank=True)
    fuel_gas_pipe_diameter = models.PositiveIntegerField(blank=True)
    fuel_gas_pipe_material = models.CharField(max_length=55, help_text="Metal")
    
    propane_capacity = models.PositiveIntegerField(blank=True)
    propane_underground = models.BooleanField(default=False)
    propane_setback_to_structures = models.PositiveIntegerField(blank=True)

    def __str__(self) -> str:
        return f"{self.number}-Plb"

    def add_notes(self):
        if self.wh_type or self.wh_capacity:
            self.notes.append("At inspection provide the CF2R and the installation instructions.")

    class Meta:
        ordering = ["number"]
        verbose_name = "Plumbing Permits"
        verbose_name_plural = "Plumbing Permits"
