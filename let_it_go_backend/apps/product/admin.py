from typing import Sequence

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from let_it_go_backend.apps.product.models import Product


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Product._meta.get_fields()]
    search_fields: Sequence[str] = ("title", "description", "category")
    list_filter = (
        "category",
        "condition",
        "owner",
        ("created_date", admin.DateFieldListFilter),
        ("modified_date", admin.DateFieldListFilter),
    )
