from typing import Any

from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse
from django.urls import path
from django.views.generic import TemplateView, CreateView

from _bp.Demolition.models import Demolition
from _bp.Demolition import config


class DemoInfo(TemplateView):
    template_name = "bp_demo.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "subject": "Demolition",
                "codes": "California Building Code and California Residential Code.",
                "licenses": [
                    "A: General Engineering",
                    "B: General",
                    "B-2: Residential Remodeling Contractor",
                    "C-21: Building Moving/Demolition Contractor",
                ],
                "review_init": "three weeks",
                "review-add": "one week",
                "additional_forms": [],
                "app_url": "app/",
                "subtypes": "config.subtypes",
            }
        )
        return context


class DemoApp(CreateView):
    model = Demolition
    template_name = "bp_demo_app.html"
    fields = [
        # 'number_of_structures',
        "demolition_area",
        # 'description',
        # 'address',
        # 'apn',
        # 'related',
        # 'contacts',
        "valuation",
        "owner_builder_form",
        "owner_rep_form",
        "CSLB_Forms",
        "employee_authorization",
    ]

    def get(
        self,
        request: HttpRequest,
        selectedSubtype="bldgDemo",
        *args: str,
        **kwargs: Any
    ) -> HttpResponse:
        return super().get(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.receive()
        return super().post(request, *args, **kwargs)
