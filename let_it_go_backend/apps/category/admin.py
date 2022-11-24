from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from let_it_go_backend.apps.category.models import Category


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass
