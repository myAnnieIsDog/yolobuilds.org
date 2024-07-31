from typing import Any

from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse
from django.urls import path
from django.views.generic import TemplateView, CreateView

from _bp.NewCommercial.newCom import Commercial


class CommercialApp(CreateView):
    model = Commercial
    template_name = "bp_com_app.html"


urlpatterns = [
    path("", TemplateView.as_view(template_name="bp_demo_info.html")),
    path("app/", CommercialApp.as_view()),
]
