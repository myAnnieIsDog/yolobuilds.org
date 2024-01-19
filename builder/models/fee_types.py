from django.db import models
from django.db import models


class Account(models.Model): 
    fund = models.CharField(max_length=4, blank=True)
    fund_label = models.CharField(max_length=55, blank=True)
    share = models.DecimalField(max_digits=3, decimal_places=2, default=1.00)
    unit = models.CharField(max_length=4, blank=True)
    unit_label = models.CharField(max_length=55, blank=True)
    unit_description = models.CharField(max_length=255, blank=True)
    cost_center = models.CharField(max_length=6, blank=True)
    gl_account = models.CharField(max_length=6, blank=True)
    cams = models.CharField(max_length=9, blank=True)
    infor_activity = models.CharField(max_length=7, blank=True)
    infor_account = models.CharField(max_length=5, blank=True)
    ledger = models.CharField(max_length=20, blank=True)
    
    def __str__(self) -> str:
        return self.unit_label
    
    class Meta():
        ordering = ["fund", "unit", "cost_center"]
        verbose_name = "Account"
        verbose_name_plural = "Accounts"


class FeeType(models.Model): 
    fee_account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="acct")
    fee_group = models.CharField(max_length=255)
    fee_name = models.CharField(max_length=255, unique=True)
    policy = models.TextField(max_length=1000, blank=True)
    authorization = models.CharField(max_length=255, blank=True)
    adopted = models.DateField(null=True, blank=True)
    revised = models.DateField(null=True, blank=True)
    expires = models.DateField(null=True, blank=True)
    tier_base_qty = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    tier_base_fee = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    rate = models.FloatField(default=5000000) # round to prevent Float errors
    units = models.CharField(max_length=255, default="each")
    rate_check = models.CharField(max_length=255, blank=True) 
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.fee_name 
    
    class Meta():
        ordering = ["fee_name"]
        verbose_name = "Fee Type"
        verbose_name_plural = "Fee Types"
