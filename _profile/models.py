from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from openpyxl import Workbook, load_workbook

base = "_profile"


def leading_zeros(seq, L: int) -> str:
    # call this function to add leading zeros and return a string.
    while len(str(seq)) < L:
        seq = f"0{seq}"
    return seq


class Agency(models.Model):
    name = models.CharField(max_length=55, unique=True)
    full = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.full

    class Meta:
        ordering = ["name"]
        verbose_name = "Agency"
        verbose_name_plural = "Agencies"

    def read_excel(path=""):
        wb = load_workbook(f"{path}/")

    def save_excel(path=""):
        pass


class Certification(models.Model):
    agency = models.CharField("Agency Acronym", max_length=15, unique=True)
    agency_long = models.CharField("Agency Full Name", max_length=255, unique=True)
    cert = models.CharField("Cert. Code", max_length=7, unique=True)
    cert_long = models.CharField("Certification Type", max_length=255, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.license_long

    class Meta:
        ordering = ["cert"]
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"


class Department(models.Model):
    name = models.CharField(max_length=25, unique=True)
    full = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.full

    class Meta:
        ordering = ["name"]
        verbose_name = "Department"
        verbose_name_plural = "Departments"


class Division(models.Model):
    name = models.CharField(max_length=255, unique=True)
    dba = models.CharField(max_length=55, unique=True)
    prefix = models.CharField(max_length=5, unique=True)
    year = models.CharField(max_length=4, default=timezone.now().strftime("%Y"))
    sequence = models.CharField(max_length=12, default="0001")
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Division"
        verbose_name_plural = "Divisions"

    def __str__(self) -> str:
        return self.prefix

    def next(record_prefix, record_year):
        # For the given prefix get last used record year and number
        n = Division.objects.get(prefix=record_prefix)

        # Annual reset or increment. BL should never reset.
        if n.year != record_year and n.prefix != "BL":
            n.year = record_year
            n.seq = "0000"
        else:
            n.seq = leading_zeros(str(int(n.sequence) + 1, 4))

        n.save()
        return f"{n.prefix}{n.year}-{n.seq}"


class Profile(models.Model):
    user_link = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="user_profile",
    )
    user = models.CharField(max_length=255, blank=True)
    first = models.CharField("First Name", max_length=255, blank=True)
    last = models.CharField("Last Name", max_length=255, blank=True)
    company = models.CharField("Company Name", max_length=255, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    active = models.BooleanField(default=True)
    recent = [""]

    # Contractors and Designers
    cert_agency = models.CharField(max_length=10, blank=True)
    cert_type = models.CharField(max_length=10, blank=True)
    cert_number = models.CharField(max_length=30, blank=True)
    cert_expires = models.DateField(null=True, blank=True)
    work_comp_agency = models.DateField(null=True, blank=True)
    work_comp_number = models.DateField(null=True, blank=True)
    verified = models.DateField()

    # Addition Information for Staff and Agency Partners
    agency = models.CharField(max_length=55, blank=True)
    department = models.CharField(max_length=55, blank=True)
    division = models.CharField(max_length=55, blank=True)
    reviewer = models.BooleanField(default=False)
    inspector = models.BooleanField(default=False)
    alt_contact_name = models.CharField(max_length=255, blank=True)
    alt_contact_email = models.CharField(max_length=255, blank=True)
    alt_contact_phone = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["first", "last"]
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self) -> str:
        return f"{self.last}, {self.first}"

    def create_user(self):
        """Update User if existing."""
        a = User()
        a.username = f"{self.first[0:1].lower()}{self.last.lower()}"
        a.email = self.email
        a.first_name = self.first
        a.last_name = self.last
        a.save()
