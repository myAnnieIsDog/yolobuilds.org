from django.shortcuts import get_object_or_404, get_list_or_404, render


from .models import Permit


def index(request):
    p = Permit.objects.all()
    context = {"permit_list": p}
    return render(request, "permit_list.html", context)
