from django.urls import path
from django.views.generic import TemplateView

from _land import views


urlpatterns = [
    path(
        "",
        TemplateView.as_view(
            template_name="bp_home.html",
            extra_context={
                "header": "Building Permits",
                "headDescription": "This is Yolo Builds, the permit application and tracking tool for Yolo County Building Division.",
            },
        ),
    ),
    path("address/", views.AddressList.as_view()),
]
