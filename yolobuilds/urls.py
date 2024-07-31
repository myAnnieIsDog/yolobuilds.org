from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

admin.site.site_title = "Yolo Builds"
admin.site.site_header = "Yolo Builds"
admin.site.index_title = "Site Administration"

urlpatterns = [
    path("", include("_base.urls")),
    path("admin/", admin.site.urls),
    path("bl/", include("_bl.urls")),
    path("bp/", include("_bp.urls")),
    path("ce/", include("_ce.urls")),
    path("fiscal/", include("_fiscal.urls")),
    path("land/", include("_land.urls")),
    path("pw/", include("_pw.urls")),
    path("zf/", include("_zf.urls")),
    # path("__debug__/", include("debug_toolbar.urls")),
]
