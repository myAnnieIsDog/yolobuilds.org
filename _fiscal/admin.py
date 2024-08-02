from django.contrib.admin import StackedInline
from django.contrib import admin

from . import models


@admin.register(models.FeeType)
class FeeTypeAdmin(admin.ModelAdmin):
    pass
