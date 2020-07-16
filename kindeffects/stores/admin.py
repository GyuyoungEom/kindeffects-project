from django.contrib import admin
from .models import Store
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

class StoreAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(Store, StoreAdmin)