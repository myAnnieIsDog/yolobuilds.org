from django.urls import path
from django.views.generic import TemplateView

from _bp.views_types import DemoInfo, DemoApp


urlpatterns = [
    path("", TemplateView.as_view(template_name="bp.html")),
    path("all/", TemplateView.as_view(template_name="bp_all.html")),
    path("<int:yr>/", TemplateView.as_view(template_name="bp_year.html")),
    path("<int:yr>/<str:numb>/", TemplateView.as_view(template_name="bp_permit.html")),
    # path('accessory', ),
    # path('accessory/app', ),
    # path('com', ),
    # path('com/app', ),
    path("demo/", DemoInfo.as_view()),
    path("demo/app/", DemoApp.as_view()),
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
