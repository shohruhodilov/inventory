from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Laptop,Device,Mobile,Desktop


@admin.register(Laptop, Mobile, Desktop)
class ViewAdmin(ImportExportModelAdmin):
    pass
