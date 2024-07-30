from django.db import models

from .fee_types import FeeType
from .bp import BP


class Fee(models.Model):
    record = models.ForeignKey(BP, on_delete=models.PROTECT, related_name="bp_fee")
    fee_type = models.ForeignKey(FeeType, on_delete=models.PROTECT)
    qty = models.DecimalField(max_digits=20, decimal_places=7, default=1.0)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=1.00)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=1000000)
    notes = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.fee_type


class TrakitFee(models.Model):
    trakit_main_fee = models.ForeignKey(Fee, on_delete=models.PROTECT, related_name="trakit_fee")
    trakit_fee_code = models.CharField(max_length=255, null=True, blank=True)
    tech = models.CharField(max_length=255, null=True, blank=True)
    trakit_description = models.CharField(max_length=255, null=True, blank=True)
    trakit_formula = models.CharField(max_length=255, null=True, blank=True)
    trakit_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.main_fee.fee_type
    
    class Meta:
        ordering = ["trakit_main_fee"]
        verbose_name = "Fee/Payment (Trakit)"
        verbose_name_plural = "Fees/Payments (Trakit)"


class ClaritiFee(models.Model):
    clariti_main_fee = models.ForeignKey(Fee, on_delete=models.PROTECT, related_name="clariti_fee")
    clariti_fee_code = models.CharField(max_length=255, null=True, blank=True)
    tech = models.CharField(max_length=255, null=True, blank=True)
    clariti_description = models.CharField(max_length=255, null=True, blank=True)
    clariti_formula = models.CharField(max_length=255, null=True, blank=True)
    clariti_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.main_fee.fee_type
    
    class Meta:
        ordering = ["clariti_main_fee"]
        verbose_name = "Fee/Payment (Clariti)"
        verbose_name_plural = "Fees/Payments (Clariti)"
