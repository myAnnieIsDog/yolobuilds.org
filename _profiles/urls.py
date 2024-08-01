from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("contacts/", views.contacts, name="contacts"),
]
