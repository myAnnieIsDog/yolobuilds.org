from typing import Any

from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path
from django.views.generic import TemplateView, CreateView

from _bp.Demolition.models import Demolition
from _bp.Demolition.config import subtypes


class LicenseInfo(TemplateView):
    template_name = "bp_demo.html"
