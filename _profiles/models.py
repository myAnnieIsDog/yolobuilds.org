from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Department(models.Model):
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.dept_code

    class Meta:
        ordering = ["code"]
        verbose_name = "Yolo Department"
        verbose_name_plural = "Yolo Department Options"


def leading_zeros(seq, L: int) -> str:
    # call this function to add leading zeros and return a string.
    while len(str(seq)) < L:
        seq = f"0{seq}"
    return seq


class Division(models.Model):
    name = models.CharField(max_length=255, unique=True)
    dba = models.CharField(max_length=55, unique=True)
    prefix = models.CharField(max_length=5, unique=True)
    year = models.CharField(max_length=4, default=timezone.now().strftime("%Y"))
    sequence = models.CharField(max_length=12, default="0001")
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Yolo DCS Division"
        verbose_name_plural = "Yolo DCS Divisions"

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
        User, on_delete=models.PROTECT, null=True, blank=True
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
    reviewer = models.BooleanField(default=False)
    inspector = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    recent = [""]

    class Meta:
        ordering = ["first", "last"]

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


class Staff(models.Model):
    profile_link = models.OneToOneField(Profile, on_delete=models.PROTECT)
    profile = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    division = models.CharField(max_length=255, blank=True)
    supervisor = models.CharField(max_length=255, blank=True)
    supervisor_email = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.profile.user.username

    class Meta:
        ordering = ["department", "division", "profile"]
        verbose_name = "Yolo DCS Employee"
        verbose_name_plural = "Yolo DCS Employees"


class AngencyPartners(models.Model):
    profile_link = models.OneToOneField(Profile, on_delete=models.PROTECT)
    profile = models.CharField(max_length=255, null=True, blank=True)
    agency = models.CharField("Agency Nickname", max_length=25, null=True, blank=True)
    full_agency = models.CharField(
        "Agency Full Name", max_length=255, null=True, blank=True
    )
    alt_contact_name = models.CharField(max_length=255, null=True, blank=True)
    alt_contact_email = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.profile.user.username

    class Meta:
        ordering = ["agency", "profile"]
        verbose_name = "Yolo DCS Partner"
        verbose_name_plural = "Yolo DCS Partners"


class ContactType(models.Model):
    role = models.CharField(max_length=55)
    description = models.TextField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.role

    class Meta:
        ordering = ["description"]
        verbose_name = "Contact Type"
        verbose_name_plural = "Contacts Types"


class Contacts(models.Model):
    profile_link = models.OneToOneField(Profile, on_delete=models.PROTECT)
    profile = models.CharField(max_length=255)
    contact_type = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.profile

    class Meta:
        ordering = ["profile"]
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class CertificateType(models.Model):
    agency = models.CharField("Agency Acronym", max_length=15, unique=True)
    agency_long = models.CharField("Agency Full Name", max_length=255, unique=True)
    cert = models.CharField("Cert. Code", max_length=7, unique=True)
    cert_long = models.CharField("Certification Type", max_length=255, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.license_long

    class Meta:
        ordering = ["cert"]
        verbose_name = "Certification Type"
        verbose_name_plural = "Certification Types"


class Certificate(models.Model):
    cert_holder_link = models.ForeignKey(Profile, on_delete=models.PROTECT)
    cert_holder = models.CharField(max_length=255)
    cert_type = models.CharField(max_length=255)
    cert_number = models.CharField(max_length=255)
    expiration_date = models.DateField(null=True, blank=True)
    verified_valid = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.license_holder} {self.license_type}"

    class Meta:
        ordering = ["cert_holder", "cert_type"]
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"
