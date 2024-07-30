from django.db import models

from .bp import BP
from .record_types import Type


class Electrical(BP):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    service_changeout = models.BooleanField(default=False)
    service_phases = models.PositiveIntegerField(default=1)
    service_voltage = models.CharField(max_length=255, default="120/240 V")
    service_current = models.PositiveIntegerField(default=150, help_text="A")
    serving = models.CharField(max_length=255, default='A Single Residential Dwelling Unit')

    general_lighting_and_receptacles = models.PositiveIntegerField(blank=True, help_text="Square feet of the area served")
    pv_solar_roof = models.PositiveIntegerField(blank=True, help_text="kW ac")
    solarAPP = models.BooleanField(default=False)
    pv_solar_ground = models.PositiveIntegerField(blank=True, help_text="kW ac")  
    ess_current = models.PositiveIntegerField(blank=True, help_text="24 A")
    ess_capacity = models.PositiveIntegerField(blank=True, help_text="14 kWh")
    evcs = models.PositiveIntegerField(blank=True, help_text="24 A")
    generator_power = models.PositiveIntegerField(blank=True, help_text="14 kWh")
    generator_fuel = models.CharField(max_length=255, default="Propane")
    motor_loads = models.PositiveIntegerField(blank=True)

    review_days = models.PositiveIntegerField(default=10)
    reviews = ["Bldg Electrical"]
    inspections = ["** PERMIT FINAL **"]
    notes = []

    def __str__(self) -> str:
        return f"{self.number}-Elc"

    def add_reviews():
        pass
    
    def add_fees():
        pass
    
    def add_insp():
        pass

    def add_notes(self):   
        if self.solarAPP:
            self.notes.append("Plans approved by SolarAPP+ can start work immediately, even if there is an error processing this permit application. At inspection provide the SolarAPP+ checklist.")

        if self.ess_current or self.ess_capacity:
            self.notes.append("At inspection provide the Energy Storage System (Battery) manufacturer's installation instructions.")
        
        if self.generator_power or self.generator_fuel:
            self.notes.append("At inspection provide the Generator manufacturer's installation instructions.")
        
        if self.evcs:
            self.notes.append("At inspection provide the EVCS manufacturer's installation instructions.")

        if self.pv_solar_ground:
            self.notes.append("At inspection provide the manufacturer's installation instructions for all Solar Equipment, including panels, dc-dc converters (optimizers), micro- or central-inverters, rapid shut-down, disconnects, racking, foundation systems, etc.")

        elif self.pv_solar_roof:
            self.notes.append("At inspection provide the manufacturer's installation instructions for all Solar Equipment, including panels, dc-dc converters (optimizers), micro- or central-inverters, rapid shut-down, disconnects, racking, etc.")

    class Meta:
        ordering = ["number"]
        verbose_name = "Electrical Permit"
        verbose_name_plural = "Electrical Permits"
