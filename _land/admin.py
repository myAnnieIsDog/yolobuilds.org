from django.contrib.admin import StackedInline
from django.contrib import admin

import _land.models as models
from _land.apps import Land


@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    pass
