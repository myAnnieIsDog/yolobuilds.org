from django.contrib import admin
from django.contrib.admin import StackedInline
from django.contrib import admin


from _bl import models


@admin.register(models.License)
class FeeTypeAdmin(admin.ModelAdmin):
    pass
