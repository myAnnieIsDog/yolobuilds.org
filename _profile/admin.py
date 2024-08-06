from django.contrib import admin

from .models import (
    Agency,
    Department,
    Division,
    Profile,
    Certification,
)


@admin.register(Agency)
class AngencyPartnersAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
    # list_display = ["dept_code", "department"]
    # list_display_links = ["dept_code", "department"]


# @admin.register(Division)
# class DivisionAdmin(admin.ModelAdmin):
#     pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    pass
