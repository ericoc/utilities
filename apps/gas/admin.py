from django.contrib import admin

from .models import GasUsage


# Create and register natural gas usage admin model.
@admin.register(GasUsage)
class GasUsageAdmin(admin.ModelAdmin):
    """Natural gas usage administration."""

    date_hierarchy = "month"
    fieldsets = (
        ("Month", {"fields": ("month",)},),
        ("Usage", {"fields": ("ccf",)},)
    )
    list_display = readonly_fields = ("month", "ccf",)
    model = GasUsage
    ordering = ("-month",)
    show_facets = admin.ShowFacets.ALWAYS
    show_full_result_count = True
    verbose_name = verbose_name_plural = "Natural Gas Usage"

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
