from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [path("", views.ProfilesView.as_view(), name="profile")]
