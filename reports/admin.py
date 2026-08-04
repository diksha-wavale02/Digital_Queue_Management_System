from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):

    list_display = (
        'report_name',
        'report_type',
        'total_tokens',
        'completed_tokens',
        'cancelled_tokens',
        'average_wait_time',
        'generated_date',
    )

    list_filter = (
        'report_type',
        'generated_date',
    )

    search_fields = (
        'report_name',
    )

    ordering = (
        '-generated_date',
    )

    list_per_page = 10