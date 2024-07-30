from django.contrib.auth.models import User
from django.db import models
import requests

from .profiles import Profile
from .fees import Fee


class PaymentMethod(models.Model):
    method = models.CharField(max_length=55, unique=True)
    policy = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.method

    class Meta:
        verbose_name = "Payment Method"
        verbose_name_plural = "Payment Methods"


class Payment(models.Model):
    fees = models.ManyToManyField(Fee)
    method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    paid_by = models.ForeignKey(Profile, on_delete=models.PROTECT)
    check_number = models.CharField(max_length=255, null=True, blank=True)
    receipt_number = models.PositiveSmallIntegerField(null=True)
    collected_by = models.ForeignKey(User, on_delete=models.PROTECT)
    deposit = models.BooleanField(default=False)
    refund = models.BooleanField(default=False)
    notes = models.TextField(max_length=255)


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
        **kwargs
    ):
        params = {
            "ssl_pin": ssl_pin,
            "ssl_transaction_type": ssl_transaction_type,
            "ssl_amount": ssl_amount, 
            "merchant_id": merchant_id,
            "merchant_user_id": merchant_user_id,
            "merchant_pin": merchant_pin,
        }
        demo = "demo." # comment-out for production url's to use the default empty string.
        token_url = (f"https://api.{demo}convergepay.com/hosted-payments/transaction_token")
        response = requests.post(token_url, params)  
        print(response)
        response.raise_for_status()
        if response.status_code == 200:
            header = (f"Location: https://api.{demo}convergepay.com/hosted-payments?ssl_txn_auth_token=$sessiontoken")
            return requests.post(header)
        else:
            return f"HTTP Status: {response.status_code}. {response}"

    # print(converge(ssl_amount = 0.50))
