from django.urls import path
from django.views.generic import DetailView

from .models.fees import Fee, TrakitFee, ClaritiFee
from .models.fee_types import Account, FeeType
from .models.fee_payments import PaymentMethod, Payment


class FiscalDetailView(DetailView):
    template_name = "layout_form.html"
    model = FeeType
    fields = "__all__"
    extra_context = {
        "heading": "Fee Types", 
        "intro": "This is a list of all of the fees charged by Yolo Builds."
    }


urlpatterns = [
    path('fees/', FiscalDetailView.as_view())
]