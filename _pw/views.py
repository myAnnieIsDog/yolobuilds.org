from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Public Works is under construction.")
