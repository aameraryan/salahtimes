from django.contrib import admin
from .models import Masjid, MasjidStaff
from import_export.admin import ImportExportModelAdmin


class MasjidStaffInline(admin.TabularInline):
    model = MasjidStaff
    extra = 0


class MasjidAdmin(ImportExportModelAdmin):
    list_display = ("name", "get_last_updated_text_admin", "get_staff_count", "fajar", "zuhar", "asar", "maghrib", "isha", "juma")
    inlines = [MasjidStaffInline, ]
    actions = ['export']


admin.site.register(Masjid, MasjidAdmin)


class MasjidStaffAdmin(admin.ModelAdmin):
    list_display = ("masjid", "name", "phone", "action_count", "get_created_on")
    readonly_fields = ("created_on", )


admin.site.register(MasjidStaff, MasjidStaffAdmin)

