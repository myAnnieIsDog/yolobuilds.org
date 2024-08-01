from django.db import models

from _bp.bp import BP
from _base.record_types import Type


class Demolition(BP):
    record_type = models.ForeignKey(
        Type, on_delete=models.PROTECT, null=True, blank=True
    )

    suffix = "-Demo"
    type_of_structure = models.CharField(max_length=55, null=True, blank=True)
    demolition_area = models.CharField(max_length=55)
    options = {
        "accessory": "Accessory",
        "commercial": "Commercial",
        "residential": "Residential",
        "partial": "Partial",
        "pool": "Pool",
    }
    subtype = models.CharField(max_length=55, choices=options)

    def __str__(self) -> str:
        return f"{self.number}-Demo"

    def add_reviews(self):
        self.reviews.add(review_type__startswith="Bldg Demo")

    def add_inspections(self):
        self.inspections.add(inspection_type__startswith="Demo")

    def add_fees(self):
        self.fees.add(fee_name="Demolition")
        self.fees.add(fee_name="Demolition of Swimming Pool")

    class Meta:
        ordering = ["number"]
        verbose_name = "Demolition Permits"
        verbose_name_plural = "Demolition Permits"
