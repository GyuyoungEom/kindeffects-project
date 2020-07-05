from django.contrib import admin
from .models import User
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

class AccountsAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(User, AccountsAdmin)