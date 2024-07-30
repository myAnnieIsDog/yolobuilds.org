from django.contrib.admin import StackedInline 
from django.contrib import admin

from .models.__init__ import *


@admin.register(FeeType)
class FeeTypeAdmin(admin.ModelAdmin):
    pass


##########################################################################
""" Profiles """
##########################################################################
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactType)
class ContactTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ["agency", "full_agency"]
    list_display_links = ["agency", "full_agency"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["dept_code", "department"]
    list_display_links = ["dept_code", "department"]


class LicenseTypeInline(admin.TabularInline):
    model = LicenseType
    extra = 0
@admin.register(LicenseAgency)
class LicenseAgencyAdmin(admin.ModelAdmin):
    verbose_name = "Licensing Agency"
    verbose_name_plural = "Licensing Agencies"
    # inlines = [LicenseTypeInline]


@admin.register(LicenseType)
class LicenseTypeAdmin(admin.ModelAdmin):
    verbose_name = "License Type"
    verbose_name_plural = "License Types"


@admin.register(LicenseHolder)
class LicenseHolderAdmin(admin.ModelAdmin):
    verbose_name = "Profile (license holders)"
    verbose_name_plural = "Profiles (license holders)"


class LicenseHolderInline(admin.TabularInline):
    model = LicenseHolder
    extra = 0
class YoloCountyPartnersInline(admin.TabularInline):
    model = YoloCountyPartners
    extra = 0
class StaffInline(admin.TabularInline):
    model = Staff
    extra = 0
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    verbose_name = "Profile (all contacts)"
    verbose_name_plural = "Profiles (all contacts)"
    inlines = [
        LicenseHolderInline, 
        YoloCountyPartnersInline, 
        StaffInline
    ]


@admin.register(Staff)
class ProfilesAdmin(admin.ModelAdmin):
    verbose_name = "Profile (staff)"
    verbose_name_plural = "Profiles (staff)"


@admin.register(YoloCountyPartners)
class ProfilesAdmin(admin.ModelAdmin):
    verbose_name = "Profile (partners)"
    verbose_name_plural = "Profiles (partners)"


##########################################################################
""" Records """
##########################################################################
@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["tag", "policy"]
    list_display_links = ["tag", "policy"]
    ordering = ["tag"]

@admin.register(Restriction)
class RestrictionAdmin(admin.ModelAdmin):
    pass

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["status", "policy", "build", "occupy"]
    list_editable = ["policy", "build", "occupy"]
    ordering = ["status"]

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["division", "prefix", "type", "suffix", "policy"]
    list_display_links = ["division", "prefix", "policy"] 
    list_editable = ["type", "suffix"]


##########################################################################
""" Reviews """
##########################################################################
@admin.register(ReviewCycle)
class ReviewCycleAdmin(admin.ModelAdmin):
    pass

@admin.register(ReviewCycleResult)
class ReviewCycleResult(admin.ModelAdmin):
    pass

@admin.register(ReviewGroup)
class ReviewGroupTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(ReviewStatus)
class ReviewStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(ReviewType)
class ReviewTypeTypeAdmin(admin.ModelAdmin):
    pass

class ReviewCycleInline(StackedInline):
    model = ReviewCycle
    extra = 0
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    inlines = [ReviewCycleInline]

##########################################################################
""" End File """
##########################################################################