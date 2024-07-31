from django.contrib import admin

##########################################################################
""" Profiles """


##########################################################################

"""

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ContactType)
class ContactTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ["agency", "full_agency"]
    list_display_links = ["agency", "full_agency"]


@admin.register(models.Department)
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


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    verbose_name = "Profile (all contacts)"
    verbose_name_plural = "Profiles (all contacts)"
    inlines = [LicenseHolderInline, YoloCountyPartnersInline, StaffInline]


@admin.register(Staff)
class ProfilesAdmin(admin.ModelAdmin):
    verbose_name = "Profile (staff)"
    verbose_name_plural = "Profiles (staff)"


@admin.register(YoloCountyPartners)
class ProfilesAdmin(admin.ModelAdmin):
    verbose_name = "Profile (partners)"
    verbose_name_plural = "Profiles (partners)"


"""
