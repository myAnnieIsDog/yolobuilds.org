from django.contrib.admin import StackedInline
from django.contrib import admin

from . import models


@admin.register(models.Division)
class DivisionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["tag", "policy"]
    list_display_links = ["tag", "policy"]
    ordering = ["tag"]


@admin.register(models.RecordStatus)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["status", "policy", "build", "occupy"]
    list_editable = ["policy", "build", "occupy"]
    ordering = ["status"]


@admin.register(models.RecordType)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["division", "type", "suffix", "policy"]
    list_display_links = ["division", "policy"]
    list_editable = ["type", "suffix"]
