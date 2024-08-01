from django.http import HttpResponse
from django.shortcuts import render

from . import models
from .models import (
    Account,
    FeeGroup,
    FeeType,
    FeeInstance,
    TrakitFee,
    ClaritiFee,
    PaymentMethod,
    Payment,
)


def config(request):
    return render(
        request,
        "fiscal_config.html",
        context={
            "accounts": models.Account.objects.all(),
            "fee_groups": models.FeeGroup.objects.all(),
            "fee_types": models.FeeType.objects.all(),
            "trakit": models.TrakitFee.objects.all(),
            "clariti": models.ClaritiFee.objects.all(),
            "pay_method": models.PaymentMethod.objects.all(),
        },
    )


def fees(request):
    return render(
        request,
        "fiscal_fee_list.html",
        context={
            # actual context is commented out to allow testing:
            # "fees": models.FeeInstance.objects.all(),
            # The following context is for testing.
            "fees": [
                {
                    "record": "BP24-001",
                    "group": "BP Admin",
                    "name": "Permit Application",
                    "qty": "1",
                    "units": "each",
                    "amount": "$65.00",
                    "balance": "$65.00",
                    "submittal": "Yes",
                    "account": "0000-0000-0000-0000",
                    "notes": "This is a test of the fee note system.",
                },
                {
                    "record": "BP24-001",
                    "group": "BP Admin",
                    "name": "Permit Issuance",
                    "qty": "1",
                    "units": "each",
                    "amount": "$85.00",
                    "balance": "$85.00",
                    "submittal": "No",
                    "account": "0000-0000-0000-0000",
                    "notes": "This is a test of the fee note system.",
                },
            ]
        },
    )


def payments(request):
    return render(
        request,
        "fiscal_payment_list.html",
        context={
            "payents": models.Payment.objects.all(),
        },
    )
