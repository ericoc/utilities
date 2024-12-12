from django.contrib import admin

from .models import ElectricUsage


# Create and register electric usage admin model.
@admin.register(ElectricUsage)
class ElectricUsageAdmin(admin.ModelAdmin):
    """Electric usage administration."""

    date_hierarchy = "hour"
    fieldsets = (
        ("Hour", {"fields": ("hour",)},),
        ("Usage", {"fields": ("kwh",)},)
    )
    list_display = readonly_fields = ("hour", "kwh",)
    model = ElectricUsage
    ordering = ("-hour",)
    show_facets = admin.ShowFacets.ALWAYS
    show_full_result_count = True
    verbose_name = verbose_name_plural = "Electric Usage"

    def has_module_permission(self, request) -> bool:
        if request.user and not request.user.is_anonymous:
            return request.user.is_superuser
        return False

    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_view_permission(self, request, obj=None) -> bool:
        return self.has_module_permission(request)
