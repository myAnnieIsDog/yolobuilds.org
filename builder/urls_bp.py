from django.urls import path
from django.views.generic import TemplateView

# from .views.bp_com import 
from .views.bp_demo import DemoInfo, DemoApp


urlpatterns = [
    path('', TemplateView.as_view(template_name="bp_home.html")),
    # path('com', ),
    # path('com/app', ),
    path('demo/', DemoInfo.as_view()),
    path('demo/app/', DemoApp.as_view()),
    # path('elc', ),
    # path('elc/app', ),
    # path('exist', ),
    # path('exist/app', ),
    # path('fire', ),
    # path('fire/app', ),
    # path('flood', ),
    # path('flood/app', ),
    # path('grade', ),
    # path('grade/app', ),
    # path('mch', ),
    # path('mch/app', ),
    # path('plb', ),
    # path('plb/app', ),
    # path('pool', ),
    # path('pool/app', ),
    # path('res', ),
    # path('res/app', ),
    # path('util', ),
    # path('util/app', ),
]