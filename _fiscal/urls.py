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
            },
        ),
    ),
]
