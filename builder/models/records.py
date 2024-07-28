from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

from .profile_staff import Division


class Status(models.Model): 
    status = models.CharField(max_length=30, unique=True)
    policy = models.CharField(max_length=255)
    build = models.BooleanField(default=False)
    occupy = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.status
    
    class Meta:
        ordering = ["status"]
        verbose_name = "Record Status"
        verbose_name_plural = "Record Statuses"

    
class Record(models.Model):
    number = models.CharField(max_length=55, unique = True)
    division = models.ForeignKey(Division, on_delete=models.PROTECT, null = True, blank = True, related_name="%(app_label)s_%(class)s_division")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null = True, blank = True, related_name="%(app_label)s_%(class)s_status")

    description = models.CharField(max_length=55, blank=True)

    """ When creating a record search for address AND parcel. 
    Use dialog to encourage selection of an address when the 
    applicant chooses a parcel that has associated addresses. """
    location_type = ContentType()  # Either an address or apn
    location_id = models.PositiveSmallIntegerField(null=True, blank = True)
    location = GenericForeignKey(location_type, location_id)

    
    def set_number(self):
        year = timezone.now().strftime("%Y")
        sequence = Division.next(self.prefix, year)
        return f"{self.prefix}{year}-{sequence}-{self.suffix}"

    class Meta():
        abstract = True
        # ordering = ["number"]
        # verbose_name = "Record"
        # verbose_name_plural = "Records"
