from typing import Any

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.views.generic import ListView, DetailView

from .models import SiteAddress, Parcel, District


def index(request):
    return HttpResponse("Land Base is under construction.")


class ParcelSearch(ListView):
    model = Parcel
    template_name = "location/apn_search.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class ParcelDetail(DetailView):
    model = Parcel
    template_name = "location/apn_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["districts"] = [District.objects.filter(parcel=self)]
        context["addresses"] = [SiteAddress.objects.filter(parcel=self)]
        # context["cases"] = [CE.objects.filter(parcel=self)]
        # context["licenses"] = [BL.objects.filter(parcel=self)]
        # context["planning"] = [ZF.objects.filter(parcel=self)]
        # context["public_works"] = [PW.objects.filter(parcel=self)]
        # context["building"] = [BP.objects.filter(parcel=self)]
        return context


class AddressList(ListView):
    model = SiteAddress
    template_name = "location/address_search.html"


class AddressDetail(DetailView):
    model = SiteAddress
    template_name = "location/address_detail.html"
