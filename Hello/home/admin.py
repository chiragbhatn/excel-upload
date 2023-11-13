from django.contrib import admin
from home.models import Contact
from import_export.admin import ImportExportModelAdmin
from .models import Port

# Register your models here.
admin.site.register(Contact)


@admin.register(Port)
class PortAdmin(ImportExportModelAdmin):
    list_display = ('ip','port','powerLevel')