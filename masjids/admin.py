from django.contrib import admin
from .models import Masjid, MasjidStaff


class MasjidStaffInline(admin.TabularInline):
    model = MasjidStaff
    extra = 0


class MasjidAdmin(admin.ModelAdmin):
    inlines = [MasjidStaffInline, ]


admin.site.register(Masjid, MasjidAdmin)


class MasjidStaffAdmin(admin.ModelAdmin):
    list_display = ("masjid", "name", "phone", "created_on", "get_created_on")
    readonly_fields = ("created_on", )


admin.site.register(MasjidStaff, MasjidStaffAdmin)

