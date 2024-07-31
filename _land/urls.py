from django.urls import path
from django.views.generic import TemplateView

from _land import views


urlpatterns = [
    path(
        "",
        TemplateView.as_view(
            template_name="_land.html",
            extra_context={
                "header": "Parcels and Addresses",
                "headDescription": "This page is for finding information about parcels and addresses.",
                "parcels": ["001-123-456", "001-123-789", "001-123-012", "001-321-456"],
                "addresses": ["10001 CR 1", "20002 CR 2", "3003 CR3"],
                "zf_zone": "RR-5",
                "flood_zone": "AE",
                "soils": "High",
                "wui": "Yes",
                "fire_district": "Willow Oak",
                "school_district": "Woodland",
                "service_district": "Wild Wings",
            },
        ),
    ),
]
