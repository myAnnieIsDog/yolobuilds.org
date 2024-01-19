from typing import Any

from django.http import HttpRequest, HttpResponse
from django.urls import path
from django.views.generic import TemplateView, CreateView

from .models.bp_demo import Demolition


class DemolitionCreateView(CreateView):
    def get():
        model = Demolition
        template_name="bp_demo_app.html"
        fields = [
            'number_of_structures',
            'demolition_area',
            'description',
            'address', 
            'apn',
            'related',
            'contacts',
            'valuation',
            'owner_builder_form',
            'owner_rep_form',
            'CSLB_Forms',
            'employee_authorization'
        ]    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.receive()
        return super().post(request, *args, **kwargs)


urlpatterns = [
    path('', TemplateView.as_view(template_name="bp_demo_info.html")),
    path('app/', DemolitionCreateView.as_view()),
]
