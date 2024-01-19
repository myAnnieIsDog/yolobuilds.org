from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """ 
    Extends User: 
    https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.User
    """
    user = models.OneToOneField(
        User, 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True, 
        related_name="user_profile")
    
    first = models.CharField("First Name", max_length=255, blank=True)
    last = models.CharField("Last Name", max_length=255, blank=True)
    company = models.CharField("Company Name", max_length=255, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    is_reviewer = models.BooleanField(default = False)
    is_inspector = models.BooleanField(default = False)

    class Meta:
        ordering = ["first", "last"]

    def __str__(self) -> str:
        return f"{self.last}, {self.first}"
    
    def create_user(self):
        """ Update User if existing. """
        a = User()
        a.username = f"{self.first[0:1].lower()}{self.last.lower()}"
        a.email = self.email
        a.first_name = self.first
        a.last_name = self.last
        a.save()
