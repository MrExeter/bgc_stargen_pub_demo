from django.contrib import admin

from . models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):

    fields = ['report_date', 'report_user', 'report_complete', 'site', 'department', 'program', 'summary', 'feedback_challenges', 'members']

    date_hierarchy = 'report_date'

    list_display = ['report_date', 'report_user', 'site', 'department', 'program', 'report_complete']
    list_filter = ['report_user', 'site', 'department', 'report_complete']

    search_fields = ['program', 'report_user__username']

