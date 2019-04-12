import django_tables2 as tables
from django_tables2.utils import A
# from django.urls import reverse
# from django.core.urlresolvers import reverse
from django.urls import reverse

# from reports.models import Report
from .models import User


class UserTable(tables.Table):
    pk = tables.LinkColumn('accounts:detail', args=[A('pk')], verbose_name='User ID')

    employee = tables.Column(accessor='get_full_name.title', verbose_name='Employee', orderable=False)

    class Meta:
        model = User
        fields = ('pk', 'employee', 'username', 'email')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no users matching the search criteria..."


class UserReportTable(tables.Table):
    pk = tables.LinkColumn('reports:detail', args=[A('pk')], verbose_name='Report ID')

    # view_edit_delete = tables.TemplateColumn(TEMPLATE, orderable=False)

    report_date = tables.DateColumn(format='j-N-Y')
    report_user = tables.Column(accessor='get_employee_name', verbose_name='Employee', orderable=False)

    class Meta:
        # model = Report
        fields = ('pk', 'report_date', 'report_user', 'site', 'department', 'program')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no reports matching the search criteria..."

    # def render_edit_link(self, report):
    #     return mark_safe('<a href=' + reverse("edit", args=[report.pk]) + '>Edit</a>')
    #
    # def render_delete_link(self, report):
    #     return mark_safe('<a href=' + reverse("delete", args=[report.pk]) + '>Delete</a>')
