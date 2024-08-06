from django.db import models
from django.utils import timezone


from _fiscal.models import FeeType
from _inspection.models import InspectionType
from _land.models import Parcel, SiteAddress
from _review.models import ReviewType
from _profile.models import Division


class RecordStatus(models.Model):
    status = models.CharField(max_length=55, unique=True)
    policy = models.CharField(max_length=255)
    build = models.BooleanField(default=False)
    occupy = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.status

    class Meta:
        ordering = ["status"]
        verbose_name = "Record Status"
        verbose_name_plural = "Record Statuses"


class RecordType(models.Model):
    division = models.ForeignKey(
        Division, on_delete=models.PROTECT, blank=True, null=True
    )
    type = models.CharField(max_length=55, blank=True, null=True)
    policy = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=7, blank=True, null=True)
    default_fees = models.ManyToManyField(FeeType, blank=True)
    default_reviews = models.ManyToManyField(ReviewType, blank=True)
    default_inspections = models.ManyToManyField(InspectionType, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.type

    class Meta:
        ordering = ["type"]
        verbose_name = "Record Type"
        verbose_name_plural = "Record Types"


class Tag(models.Model):
    tag = models.CharField(max_length=55, blank=True, unique=True)
    policy = models.TextField(max_length=255, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.tag

    class Meta:
        ordering = ["tag"]


class ContactType(models.Model):
    role = models.CharField(max_length=55)
    description = models.TextField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.role

    class Meta:
        ordering = ["description"]
        verbose_name = "Contact Type"
        verbose_name_plural = "Contact Types"


class Record(models.Model):
    number = models.CharField(max_length=55, unique=True)
    type = models.CharField(max_length=55, unique=True)
    type_link = models.ForeignKey(
        RecordType,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=55, unique=True)
    description = models.CharField(max_length=55, blank=True)
    tags = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)

    parcel_links = models.ManyToManyField(Parcel)
    parcels = models.CharField(max_length=255, blank=True)
    address_links = models.ManyToManyField(SiteAddress)
    addresses = models.CharField(max_length=255, blank=True)
    related_links = models.ManyToManyField("self", symmetrical=True)
    related = {
        "bl": [""],
        "bp": [""],
        "ce": [""],
        "pw": [""],
        "zf": [""],
        "tags": [""],
        "restrictions": [""],
        "notes": [""],
    }

    # Restrictions
    lock = models.BooleanField(default=False)
    lock_related = models.BooleanField(default=False)
    alert = models.BooleanField(default=False)
    alert_related = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.number}-{self.type.suffix}"

    class Meta:
        abstract = True
        # ordering = ["number"]
        # verbose_name = "Record"
        # verbose_name_plural = "Records"

    def new(self):
        self.number = self.division.next(
            self.type.division.prefix, timezone.now().strftime("%Y")
        )
        self.status = "Application"
