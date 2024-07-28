from typing import Any

from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse
from django.urls import path
from django.views.generic import TemplateView, CreateView

from ..models.bp_demo import Demolition


class DemoInfo(TemplateView):
    template_name = "bp_demo.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            "subject": "Demolition",
            "codes": "California Building Code and California Residential Code in their entirety",
            "licenses": [
                "A: General Engineering", 
                "B: General", 
                "B-2: Residential Remodeling Contractor", 
                "C-21: Building Moving/Demolition Contractor"
            ],
            # "initial_review_time": "three weeks",
            # "additional_review_time": "one week",
            "additional_forms": [],
            "app_url": "app/",
            "subtypes": [
                {
                    "title": "Building Demolition",
                    "value": "bldgDemo",
                    "description": "Complete removal of above ground structures up to three stories and without any hazards identified by the Chief Building Official.",
                },
                {
                    "title": "Partial Demolition",
                    "value": "partDemo",
                    "description": "For the demolition stage of a major remodel, often used to allow demolition to proceed prior to full approval of the remodel permit. This permit type is issued 'at-risk': There is no guarantee that your remodel permit will be approved, so proceed with caution during demolition activities.",
                },
                {
                    "title": "Pool Demolition",
                    "value": "poolDemo",
                    "description": "The demolition of a pool or similar below-grade structure that requires verification of compacted fill.",
                },       
            ],         
        })
        return context


class DemoApp(CreateView):
    model = Demolition
    template_name="bp_demo_app.html"
    fields = [
        # 'number_of_structures',
        'demolition_area',
        # 'description',
        # 'address', 
        # 'apn',
        # 'related',
        # 'contacts',
        'valuation',
        'owner_builder_form',
        'owner_rep_form',
        'CSLB_Forms',
        'employee_authorization'
    ]    
    
    def get(self, request: HttpRequest, selectedSubtype = "bldgDemo", *args: str, **kwargs: Any) -> HttpResponse:           
        return super().get(request, *args, **kwargs)
    

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.receive()
        return super().post(request, *args, **kwargs)


