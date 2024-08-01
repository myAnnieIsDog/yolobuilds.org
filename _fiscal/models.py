from django.db import models

from django.contrib.auth.models import User
from django.db import models
import requests


class Account(models.Model):
    name = models.CharField(max_length=55, blank=True, null=True, unique=True)
    description = models.CharField(max_length=255, blank=True)
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
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def list(Accounts):
        accounts = Accounts.objects.all()
        return accounts


class FeeGroup(models.Model):
    name = models.CharField(max_length=55, blank=True, null=True, unique=True)
    description = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)


class FeeType(models.Model):
    fee_name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    fee_account = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name="acct"
    )
    fee_group = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name="group"
    )
    description = models.CharField(max_length=255, blank=True)
    policy = models.TextField(max_length=1000, blank=True)
    authorization = models.CharField(max_length=255, blank=True)
    adopted = models.DateField(null=True, blank=True)
    revised = models.DateField(null=True, blank=True)
    expires = models.DateField(null=True, blank=True)
    tier_base_qty = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    tier_base_fee = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    rate = models.FloatField(default=5000000)  # round this to prevent Float errors
    units = models.CharField(max_length=255, default="each")
    submittal = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.fee_name

    class Meta:
        ordering = ["fee_name"]
        verbose_name = "Fee Type"
        verbose_name_plural = "Fee Types"


class FeeInstance(models.Model):
    record = models.CharField(max_length=1000, blank=True)
    group = models.CharField(max_length=255, blank=True)
    type = models.ForeignKey(FeeType, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True)
    account = models.CharField(max_length=255, blank=True)

    qty = models.DecimalField(max_digits=20, decimal_places=7, default=1.0)
    units = models.CharField(max_length=255, default="each")
    tier_base_qty = models.CharField(max_length=255, blank=True)
    tier_base_fee = models.CharField(max_length=255, blank=True)
    tier_rate = models.CharField(max_length=255, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=1.00)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=1000000)

    notes = models.TextField(max_length=255)
    submittal = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.fee_type


class TrakitFee(models.Model):
    trakit_main_fee = models.ForeignKey(
        FeeInstance, on_delete=models.PROTECT, related_name="trakit_fee"
    )
    trakit_fee_code = models.CharField(max_length=255, blank=True)
    tech = models.CharField(max_length=255, blank=True)
    trakit_description = models.CharField(max_length=255, blank=True)
    trakit_formula = models.CharField(max_length=255, blank=True)
    trakit_id = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.main_fee.fee_type

    class Meta:
        ordering = ["trakit_main_fee"]
        verbose_name = "Fee/Payment (Trakit)"
        verbose_name_plural = "Fees/Payments (Trakit)"


class ClaritiFee(models.Model):
    clariti_main_fee = models.ForeignKey(
        FeeInstance, on_delete=models.PROTECT, related_name="clariti_fee"
    )
    clariti_fee_code = models.CharField(max_length=255, blank=True)
    tech = models.CharField(max_length=255, blank=True)
    clariti_description = models.CharField(max_length=255, blank=True)
    clariti_formula = models.CharField(max_length=255, blank=True)
    clariti_id = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.main_fee.fee_type

    class Meta:
        ordering = ["clariti_main_fee"]
        verbose_name = "Fee/Payment (Clariti)"
        verbose_name_plural = "Fees/Payments (Clariti)"


class PaymentMethod(models.Model):
    method = models.CharField(max_length=55, unique=True)
    policy = models.TextField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.method

    class Meta:
        verbose_name = "Payment Method"
        verbose_name_plural = "Payment Methods"


class Payment(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    check_number = models.CharField(max_length=255, blank=True)
    collected_by = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now=True)
    deposit = models.BooleanField(default=False)
    fees = models.ManyToManyField(FeeInstance)
    method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    notes = models.TextField(max_length=255)
    paid_by = models.CharField(max_length=255, unique=True)
    receipt_number = models.CharField(max_length=55, unique=True)
    refund = models.BooleanField(default=False)

    def pay_now():
        # Process the transaction. FUTURE: integrate with Elavon/Converge.
        # Generate a pdf receipt, save it to the payments directory, link
        # the file to the related fee records, and display it to the user
        # for printing.
        pass

    def converge(
        ssl_pin="123",
        ssl_transaction_type="ccsale",
        ssl_amount="0.10",
        merchant_id="000062",
        merchant_user_id="sdoolittle",
        merchant_pin="tbd",
        demo="",
        **kwargs,
    ):
        params = {
            "ssl_pin": ssl_pin,
            "ssl_transaction_type": ssl_transaction_type,
            "ssl_amount": ssl_amount,
            "merchant_id": merchant_id,
            "merchant_user_id": merchant_user_id,
            "merchant_pin": merchant_pin,
        }
        demo = (
            "demo."  # comment-out for production url's to use the default empty string.
        )
        token_url = (
            f"https://api.{demo}convergepay.com/hosted-payments/transaction_token"
        )
        response = requests.post(token_url, params)
        print(response)
        response.raise_for_status()
        if response.status_code == 200:
            header = f"Location: https://api.{demo}convergepay.com/hosted-payments?ssl_txn_auth_token=$sessiontoken"
            return requests.post(header)
        else:
            return f"HTTP Status: {response.status_code}. {response}"

    # print(converge(ssl_amount = 0.50))
