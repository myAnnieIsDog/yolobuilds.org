from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    """
    Extends User:
    https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.User
    """
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True)
    first = models.CharField("First Name", max_length=255, blank=True)
    last = models.CharField("Last Name", max_length=255, blank=True)
    company = models.CharField("Company Name", max_length=255, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    is_reviewer = models.BooleanField(default=False)
    is_inspector = models.BooleanField(default=False)

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


class LicenseAgency(models.Model):
    agency = models.CharField("Agency Acronym", max_length=15, unique=True)
    agency_long = models.CharField("Agency Full Name", max_length=255, unique=True)

    def __str__(self) -> str:
        return self.agency

    class Meta:
        ordering = ["agency"]
        verbose_name = "Certification Agency"
        verbose_name_plural = "Certification Agencies"


class LicenseType(models.Model):
    licensing_agency = models.ForeignKey(LicenseAgency, on_delete=models.PROTECT, null=True)
    license_short = models.CharField("Licens Type", max_length=7, unique=True)
    license_long = models.CharField("Licens Type", max_length=255, unique=True)

    def __str__(self) -> str:
        return self.license_long

    class Meta:
        ordering = ["license_short"]
        verbose_name = "Certification Type"
        verbose_name_plural = "Certification Types"


class LicenseHolder(models.Model):
    license_holder = models.ForeignKey(Profile, on_delete=models.PROTECT)
    license_type = models.ForeignKey(LicenseType, on_delete=models.PROTECT)
    license_number = models.CharField(max_length=255, unique=True)
    expiration_date = models.DateField()
    verified_valid = models.BooleanField()
    # replace the following with a relationship to business license records.
    bl_number = models.CharField(
        "Yolo County Business License Number", max_length=40, blank=True
    )

    def __str__(self) -> str:
        return f"{self.license_holder} {self.license_type}"

    class Meta:
        ordering = ["license_holder", "license_type"]
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"


class ContactType(models.Model):
    role = models.CharField(max_length=55)
    description = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.role

    class Meta:
        ordering = ["description"]
        verbose_name = "Contact Type"
        verbose_name_plural = "Contacts Types"


class Contact(models.Model):
    contact = models.ForeignKey(Profile, on_delete=models.PROTECT)
    contact_type = models.ForeignKey(ContactType, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.contact} is the {self.role} on {self.record}."

    class Meta:
        ordering = ["contact"]
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Agency(models.Model):
    agency = models.CharField(max_length=25, unique=True)
    full_agency = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.agency

    class Meta:
        ordering = ["agency"]
        verbose_name = "Yolo DCS Partner Agency"
        verbose_name_plural = "Yolo DCS Partner Agencies"


class YoloCountyPartners(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.PROTECT)
    agency = models.ForeignKey(Agency, on_delete=models.PROTECT)
    alt_contact_name = models.CharField(max_length=255, null=True, blank=True)
    alt_contact_email = models.CharField(max_length=255, null=True, blank=True)
    # recent_records = models.ManyToManyField(Record)

    def __str__(self) -> str:
        return self.profile.user.username

    class Meta:
        ordering = ["agency", "profile"]
        verbose_name = "Yolo DCS Partner"
        verbose_name_plural = "Yolo DCS Partners"


class Department(models.Model):
    dept_code = models.CharField(max_length=25, unique=True)
    department = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.dept_code
    
    class Meta:
        ordering = ["dept_code"]
        verbose_name = "Yolo Department"
        verbose_name_plural = "Yolo Department Options"


class Division(models.Model): 
    prefix = models.CharField(max_length=5, unique=True) 
    division = models.CharField(max_length=30, unique=True)
    full_division = models.CharField(max_length=255, unique=True)
    year = models.CharField(max_length=55, default = timezone.now().strftime("%Y"))
    sequence = models.CharField(max_length = 12, default = "0000")

    class Meta:
        ordering = ["division"]
        verbose_name = "Yolo DCS Division"
        verbose_name_plural = "Yolo DCS Divisions"
    
    def __str__(self) -> str:
        return self.prefix
    
    def next(record_prefix, record_year):
        """ This function is mostly side-effects, and returns the next record number. """
        n = Division.objects.get(prefix=record_prefix)
        if n.year != record_year and n.prefix != "BL": 
            """ Annual Reset, except BL """
            n.year = record_year
            n.sequence = "0000"
        n.sequence = str(int(n.sequence) + 1)
        while len(n.sequence) < 4:
            """ Add leading zeros to the string. """
            n.sequence = f"0{n.sequence}"
        n.save()
        return {n.sequence}


class Staff(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.PROTECT, related_name="staff_profile")
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    division = models.ForeignKey(Division, on_delete=models.PROTECT)
    supervisor = models.CharField(max_length=255, null=True, blank=True)
    supervisor_email = models.CharField(max_length=255, null=True, blank=True)
    # recent_records = models.ManyToManyField(Record)

    def __str__(self) -> str:
        return self.profile.user.username
    
    class Meta():
        ordering = ["department", "division", "profile"]
        verbose_name = "Yolo DCS Employee"
        verbose_name_plural = "Yolo DCS Employees"
