from django.urls import path
from django.views.generic import TemplateView

from _bp.types.Demolition import views as demo

# from _bp.types.Electrical import views as elc
# from _bp.types.Existing import views as exist
# from _bp.types.Fire import views as fire
# from _bp.types.Flood import views as flood
# from _bp.types.Grading import views as grading
# from _bp.types.Mechanical import views as mch
# from _bp.types.NewResidential import views as res
# from _bp.types.NewAccessory import views as accessory
# from _bp.types.NewCommercial import views as com
# from _bp.types.Plumbing import views as plb
# from _bp.types.Pool import views as pool


urlpatterns = [
    path("", TemplateView.as_view(template_name="bp.html")),
    path("all/", TemplateView.as_view(template_name="bp_all.html")),
    path("<int:yr>/", TemplateView.as_view(template_name="bp_year.html")),
    path("<int:yr>/<str:numb>/", TemplateView.as_view(template_name="bp_permit.html")),
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
