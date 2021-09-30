from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from import_export.admin import ImportExportModelAdmin

# Register your models here.


from catalog.models import Product


@admin.register(Product)
class SendeAdmin(ImportExportModelAdmin):

    save_on_top = True
    list_per_page = 30

    list_filter = ["name", "status"]
    list_display = [
        "name",
        "price",
        "image_tag",
        "tax",
        "created_at",
        "updated_at"
    ]
