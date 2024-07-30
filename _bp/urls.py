from django.urls import path
from django.views.generic import TemplateView

from _bp.types.accessory import views as accessory
from _bp.types.com import views as com
from _bp.types.demo import views as demo
from _bp.types.elc import views as elc
from _bp.types.exist import views as exist
from _bp.types.fire import views as fire
from _bp.types.flood import views as flood
from _bp.types.grading import views as grading
from _bp.types.mch import views as mch
from _bp.types.plb import views as plb
from _bp.types.pool import views as pool
from _bp.types.res_new import views as res



urlpatterns = [
    path('', TemplateView.as_view(template_name="bp_home.html", extra_context={
        "header": "Building Permits",
        "headDescription": 
        "This is Yolo Builds, the permit application and tracking tool for Yolo County Building Division.",
    })), 

    # path('accessory', ),
    # path('accessory/app', ),
    # path('com', ),
    # path('com/app', ),
    path('demo/', demo.DemoInfo.as_view()),
    path('demo/app/', demo.DemoApp.as_view()),
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