from django.contrib import admin

from .models import WaterUsage


# Create and register water usage admin model.
@admin.register(WaterUsage)
class WaterUsageAdmin(admin.ModelAdmin):
    """Water usage administration."""

    date_hierarchy = "date"
    fieldsets = (
        ("Date", {"fields": ("date",)},),
        ("Usage", {"fields": ("gallons",)},)
    )
    list_display = readonly_fields = ("date", "gallons",)
    model = WaterUsage
    ordering = ("-date",)
    show_facets = admin.ShowFacets.ALWAYS
    show_full_result_count = True
    verbose_name = verbose_name_plural = "Water Usage"

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
