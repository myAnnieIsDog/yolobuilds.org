from django.db import models
from django.utils import timezone

from .profiles import Profile


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