from typing import Any

from django.db.models.base import Model as Model
from django.urls import path
from django.views.generic import TemplateView, ListView, DetailView

from _reviews.models import Review, ReviewCycle


class ReviewList(ListView):
    model = Review
    template_name = "reviews/list.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["reviews"] = ReviewCycle.objects.all().filter(status="Under Review")
        return context


class ReviewDetail(DetailView):
    model = Review
    template_name = "reviews/cycles.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["cycles"] = ReviewCycle.objects.all().filter(review=self.kwargs["pk"])
        return context


urlpatterns = [
    path("", TemplateView.as_view(template_name="reviews/prototype.html")),
    path("list/", ReviewList.as_view()),
    path("<int:pk>", ReviewDetail.as_view()),
]
