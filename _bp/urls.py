from django.urls import path
from django.views.generic import TemplateView

from _bp.Demolition import views as demo
from _bp.Electrical import views as elc
from _bp.Existing import views as exist
from _bp.Fire import views as fire
from _bp.Flood import views as flood
from _bp.Grading import views as grading
from _bp.Mechanical import views as mch
from _bp.NewResidential import views as res
from _bp.NewAccessory import views as accessory
from _bp.NewCommercial import views as com
from _bp.Plumbing import views as plb
from _bp.Pool import views as pool


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
    # path('accessory', ),
    # path('accessory/app', ),
    # path('com', ),
    # path('com/app', ),
    path("demo/", demo.DemoInfo.as_view()),
    path("demo/app/", demo.DemoApp.as_view()),
    # path('elc', ),
    # path('elc/app', ),
    # path('exist', ),
    # path('exist/app', ),
    # path('fire', ),
    # path('fire/app', ),
    # path('flood', ),
    # path('flood/app', ),
    # path('grading', ),
    # path('grading/app', ),
    # path('mch', ),
    # path('mch/app', ),
    # path('plb', ),
    # path('plb/app', ),
    # path('pool', ),
    # path('pool/app', ),
    # path('res', ),
    # path('res/app', ),
]
