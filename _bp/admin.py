from django.contrib.admin import StackedInline
from django.contrib import admin


"""
@admin.register(FeeType)
class FeeTypeAdmin(admin.ModelAdmin):
    pass
"""

##########################################################################
""" Records """
##########################################################################
"""
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

"""

##########################################################################
""" Reviews """
##########################################################################

"""
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

"""

##########################################################################
""" End File """
##########################################################################
