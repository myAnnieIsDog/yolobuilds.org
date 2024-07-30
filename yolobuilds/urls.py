from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

admin.site.site_title = 'Yolo Builds'
admin.site.site_header = 'Yolo Builds'
admin.site.index_title = 'Site Administration'

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html", extra_context={
        "header": "Welcome",
        "headDescription": 
        "This is Yolo County's permit application and tracking tool for Building, Planning, and Public Works permits.",
    })),
    path('admin/', admin.site.urls),
    path('bl/', include('_bl.urls')), 
    path('bp/', include('_bp.urls')),
    path('ce/', include('_ce.urls')), 
    path('pw/', include('_pw.urls')), 
    path('zf/', include('_zf.urls')), 

    path('<path:catchall>/', include('__shared.urls')),  

    # path('__debug__/', include('debug_toolbar.urls')),
]