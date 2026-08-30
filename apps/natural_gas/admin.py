from django.contrib import admin

from .models import NaturalGasUsage


# Create and register natural gas usage admin model.
@admin.register(NaturalGasUsage)
class NaturalGasUsageAdmin(admin.ModelAdmin):
    """Natural gas usage administration."""

    def format_date_to_month(self, obj):
        return obj.month.strftime("%B %Y")

    format_date_to_month.admin_order_field = "month"
    format_date_to_month.short_description = "Month"

    date_hierarchy = "month"
    fieldsets = (
        ("Month", {"fields": ("format_date_to_month",)},),
        ("Usage", {"fields": ("rounded_ccf",)},)
    )
    list_display = readonly_fields = ("format_date_to_month", "rounded_ccf",)
    list_filter = ("month",)
    model = NaturalGasUsage
    ordering = ("-month",)
    show_facets = admin.ShowFacets.ALWAYS
    show_full_result_count = True
    verbose_name = verbose_name_plural = "Natural Gas Usage"

    @admin.display(description="CCF")
    def rounded_ccf(self, obj):
        return round(obj.ccf)

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
