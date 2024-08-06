from django.contrib.admin import StackedInline
from django.contrib import admin


from . import models


##########################################################################
""" Reviews """
##########################################################################


@admin.register(models.ReviewCycle)
class ReviewCycleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ReviewCycleResult)
class ReviewCycleResult(admin.ModelAdmin):
    pass


@admin.register(models.ReviewGroup)
class ReviewGroupTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ReviewStatus)
class ReviewStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ReviewType)
class ReviewTypeTypeAdmin(admin.ModelAdmin):
    pass


##########################################################################
""" End File """
##########################################################################
