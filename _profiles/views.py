from django.http import HttpResponse
from django.shortcuts import render

from . import models

models.Agency
models.Contact
models.ContactType
models.Department
models.Division
models.LicenseAgency
models.LicenseHolder
models.LicenseType
models.Profile
models.Staff


def contacts(request):
    return render(
        request,
        "contacts_list.html",
        context={
            "contacts": [
                {
                    "first": "Joe",
                    "last": "Schmoe",
                    "company": "Golden Hammers",
                    "email": "Joe@GoldenHammers.com",
                    "phone": "530-666-9876",
                    "mailing": "12345 County Road 198",
                    "cityStZip": "West Sacramento CA 95600",
                    "license": "123456789 B",
                    "alerts": True,
                },
                {
                    "first": "Rita",
                    "last": "Schmoe",
                    "company": "Golden Hammers",
                    "email": "Rita@GoldenHammers.com",
                    "phone": "530-666-9875",
                    "mailing": "12345 County Road 198",
                    "cityStZip": "West Sacramento CA 95600",
                    "license": "123456789 B",
                    "alerts": False,
                },
            ]
        },
    )


def index(request):
    return HttpResponse("Profiles is under construction.")
