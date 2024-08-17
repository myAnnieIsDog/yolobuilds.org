from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import TemplateView

from . import models


class ProfilesView(TemplateView):
    template_name = "profiles.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["users"] = [  # models.Profile.objects.all()
            {
                "first": "Scott",
                "last": "Doolittle",
                "company": "",
                "agency": "Yolo County",
                "department": "DCS",
                "division": "Building",
                "title": "Chief Building Official",
                "email": "scott.doolittle@yolocounty.gov",
                "phone": "530-666-8609",
                "mailing": "292 W Beamer St",
                "cityStZip": "Woodland CA 95695",
                "license": "PE 75864",
                "alerts": False,
                "role": "Staff",
            },
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
                "role": "User",
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
                "role": "Contact",
            },
        ]
        return context
