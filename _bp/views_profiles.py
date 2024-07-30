from django.forms import ModelForm
from django.urls import path
from django.views.generic import DetailView, CreateView, UpdateView

# from django_recaptcha.fields import ReCaptchaField

from ..models.profiles import Profile


class ProfileForm(ModelForm):
    # captcha = ReCaptchaField()
    class Meta:
        model = Profile #, User
        fields = [
            "user", 
            # "company_name", 
            # "phone_number", 
            "address", 
            "city", 
            "state", 
            "zip", 
        ]
        # Add a method to also generate a User for the profile when generated online. The method should be optional when staff creates a profile to add to an application.


class ProfileCreateView(CreateView):
    template_name = "layout_form.html"
    model = Profile
    exclude = ["user", "display_mode", "home_page", "recent_records", 
               "modified_on", "modified_by", "create_on", "create_by"]
    extra_context = {
        "heading": "Create Profile", 
        "intro": "Use this form to create a user profile. A valid email is required to verify your profile.",
        "button_text": "Submit"}
    success_url = "profile-update"
    success_message = "The profile for %(first_name)s %(last_name)s was created successfully."  


class ProfileDetailView(DetailView):
    template_name = "layout_form.html"
    model = Profile
    fields = "__all__"
    extra_context = {
        "heading": "Update Profile", 
        "intro": "Use this form to update your user profile.", 
        "button_text": "Update"}
    success_url = "profile-update"


class ProfileUpdateView(UpdateView):
    template_name = "layout_form.html"
    model = Profile
    exclude = ["modified_on", "modified_by", "create_on", "create_by"]
    extra_context = { 
        "heading": "Update Profile", 
        "intro": "Use this form to update your user profile.", 
        "button_text": "Update"}
    success_url = "profile-update"


urlpatterns = [
    path('create/', ProfileCreateView.as_view()),
    path('detail/', ProfileDetailView.as_view()),
    path('update/', ProfileUpdateView.as_view()),
]