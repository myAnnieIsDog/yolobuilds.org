from django.db import models

from .bp import UseGroup, TypeOfConstruction, BP
from .record_types import Type


class Existing(BP):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    existing_use = models.ForeignKey(UseGroup, on_delete=models.PROTECT)
    existing_type_of_construction = models.ForeignKey(TypeOfConstruction, on_delete=models.PROTECT)
    existing_building_area = models.PositiveSmallIntegerField("Existing Building Area (square feet)", default=0)

    addition_area = models.PositiveSmallIntegerField(default=0)
    addition_use = models.CharField(max_length=255, default="R-3 Residential Dwelling")

    alteration_area = models.PositiveSmallIntegerField(default=0)
    alteration_use = models.CharField(max_length=255, default="R-3 Residential Dwelling")

    reroof_area = models.PositiveIntegerField(default=0)
    reroof_fire_class = models.CharField(max_length=1)
    reroof_cool_roof = models.BooleanField(default=False)

    ext_wall_replacement_type = models.CharField(max_length=255, default="Stucco")
    ext_wall_replacement_area = models.PositiveSmallIntegerField(default=0)
    ext_wall_replacement_fire_class = models.CharField(max_length=1)

    window_replacement_quantity = models.PositiveSmallIntegerField(default=0)
    window_replacement_like_for_like_area = models.PositiveSmallIntegerField(default=0)
    window_replacement_new_area = models.PositiveSmallIntegerField(default=0)
    window_replacement_cf1r = models.BooleanField(default=False)
    window_replacement_hazardous_locations = models.BooleanField(default=False)

    # def __str__(self) -> str:
    #     return f"{self.number}-Ex"
    
    class Meta:
        # ordering = ["number"]
        verbose_name = "Existing Building Code Permit"
        verbose_name_plural = "Existing Building Code Permits"
