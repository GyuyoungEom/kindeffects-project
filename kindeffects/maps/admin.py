from django.contrib import admin
from .models import Map,Code
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

class MapAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class CodeAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Map, MapAdmin)
admin.site.register(Code, CodeAdmin)