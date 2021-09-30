from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from order.models import Order, Status, Period

@admin.register(Period)
class StatusAdmin(ImportExportModelAdmin):

    save_on_top = True
    list_per_page = 30

    list_filter = ["period"]
    list_display = [
        "period",
        "start",
        "end",
        "created_at",
        "updated_at"
    ]

@admin.register(Status)
class StatusAdmin(ImportExportModelAdmin):

    save_on_top = True
    list_per_page = 30

    list_filter = ["name"]
    list_display = [
        "name",
        "description",
        "created_at",
        "updated_at"
    ]


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):

    save_on_top = True
    list_per_page = 30

    list_filter = ["partner", "products", "status"]
    list_display = [
        "partner",
        "products",
        "status",
        "tax",
        "grand_total",
        "created_at",
        "updated_at"
    ]

    readonly_fields = [
        "order",
    ]

    readonly_fields_edited = [
        "partner",
        "tax",
        "subtotal",
        "grand_total",
        "order",
        "products",
        "points"
    ]

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(
            OrderAdmin, self).get_readonly_fields(request, obj)

        if obj:
            return readonly_fields + self.readonly_fields_edited
        return readonly_fields
