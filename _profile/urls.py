from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("contacts/", views.contacts, name="contacts"),
    # path("create/", views.ProfileCreateView.as_view()),
    # path("detail/", views.ProfileDetailView.as_view()),
    # path("update/", views.ProfileUpdateView.as_view()),
]
