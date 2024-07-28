from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

admin.site.site_title = 'Yolo Builds'
admin.site.site_header = 'Yolo Builds'
admin.site.index_title = 'Site Administration'

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    # path('address/', include('builder.urls_address')),
    path('admin/', admin.site.urls),
    path('bp/', include('builder.urls_bp')),    
    # path('fees/', include('builder.urls_fees')),
    # path('parcel/', include('builder.urls_parcels')),     
    # path('profile/', include('builder.urls_profiles')),
    # path('review/', include('builder.urls_reviews')),
    # path('__debug__/', include('debug_toolbar.urls')),
]