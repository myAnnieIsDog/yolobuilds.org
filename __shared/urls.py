from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "",
        TemplateView.as_view(
            template_name="index.html",
            extra_context={
                "header": "Welcome",
                "headDescription": "This is Yolo County's permit application and tracking tool for Building, Planning, and Public Works permits.",
            },
        ),
    ),
    path(
        "land/",
        TemplateView.as_view(
            template_name="bp_home.html",
            extra_context={
                "header": "Building Permits",
                "headDescription": "This is Yolo Builds, the permit application and tracking tool for Yolo County Building Division.",
            },
        ),
    ),
    path(
        "fiscal/",
        TemplateView.as_view(
            template_name="bp_home.html",
            extra_context={
                "header": "Building Permits",
                "headDescription": "This is Yolo Builds, the permit application and tracking tool for Yolo County Building Division.",
            },
        ),
    ),
    path(
        "inspection/",
        TemplateView.as_view(
            template_name="bp_home.html",
            extra_context={
                "header": "Building Permits",
                "headDescription": "This is Yolo Builds, the permit application and tracking tool for Yolo County Building Division.",
            },
        ),
    ),
    path(
        "profile/",
        TemplateView.as_view(
            template_name="bp_home.html",
            extra_context={
                "header": "Building Permits",
                "headDescription": "This is Yolo Builds, the permit application and tracking tool for Yolo County Building Division.",
            },
        ),
    ),
    path(
        "review/",
        TemplateView.as_view(
            template_name="bp_home.html",
            extra_context={
                "header": "Building Permits",
                "headDescription": "This is Yolo Builds, the permit application and tracking tool for Yolo County Building Division.",
            },
        ),
    ),
    path(
        "test/",
        TemplateView.as_view(
            template_name="partials/search.html",
            extra_context={
                "header": "Test",
                "headDescription": "This URL is intended to test the rendering of various html drafts.",
            },
        ),
    ),
]
