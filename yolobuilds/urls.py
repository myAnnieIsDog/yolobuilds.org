from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

admin.site.site_title = "Yolo Builds"
admin.site.site_header = "Yolo Builds"
admin.site.index_title = "Site Administration"

urlpatterns = [
    path("", TemplateView.as_view(template_name="base_home.html")),
    path("admin/", admin.site.urls),
    path("bl/", include("_bl.urls")),
    path("bp/", include("_bp.urls")),
    path("ce/", include("_ce.urls")),
    path("fiscal/", include("_fiscal.urls")),
    path("inspections/", include("_inspections.urls")),
    path("land/", include("_land.urls")),
    path("profile/", include("_profiles.urls")),
    path("pw/", include("_pw.urls")),
    path("reviews/", include("_reviews.urls")),
    path("search/", TemplateView.as_view(template_name="base_search_advanced.html")),
    path("zf/", include("_zf.urls")),
    # path("__debug__/", include("debug_toolbar.urls")),
]
