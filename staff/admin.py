from django.contrib import admin
from .models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "employee_id",
        "department",
        "service",
        "email",
        "phone",
        "status",
        "created_at",
    )

    list_filter = (
        "department",
        "status",
    )

    search_fields = (
        "full_name",
        "employee_id",
        "email",
    )