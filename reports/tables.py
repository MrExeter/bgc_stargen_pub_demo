'''
Description - Reports Tables
@author - John Sentz
@date - 15-Nov-2018
@time - 9:04 PM
'''


import django_tables2 as tables
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_tables2.utils import A

from . models import Report


class ReportTable(tables.Table):


    TEMPLATE_VIEW = '''
           <a href="{% url 'reports:detail' record.pk %}">
           <button class="btn btn-primary btn-block"  label="View" name="{% url 'reports:detail' record.pk %}">
           <span class="far fa-eye"></span>
           View</button>
           </a>
    '''

    TEMPLATE_EDIT = '''
           <a href="{% url 'reports:report-update' record.pk %}">
           <button class="btn btn-success btn-block"  label="Edit" name="{% url 'reports:report-update' record.pk %}">
           <span class="fas fa-pencil-alt"></span>
           Edit</button>
           </a>
    '''

    TEMPLATE_DELETE = '''
           <a href="{% url 'reports:report-delete' record.pk %}">
           <button class="btn btn-danger btn-block"  label="Delete" name="{% url 'reports:report-delete' record.pk %}">
           <span class="fas fa-trash-alt"></span>
           Delete</button>
           </a>        
    '''

    pk = tables.LinkColumn('reports:detail', args=[A('pk')], verbose_name='Report ID')
    view = tables.TemplateColumn(TEMPLATE_VIEW, orderable=False, verbose_name='')
    edit = tables.TemplateColumn(TEMPLATE_EDIT, orderable=False, verbose_name='')
    delete = tables.TemplateColumn(TEMPLATE_DELETE, orderable=False, verbose_name='')
    report_date = tables.DateColumn(format='j-M-Y')
    report_user = tables.Column(accessor='get_employee_name', verbose_name='Employee', orderable=False)

    class Meta:
        model = Report
        fields = ('pk', 'report_date', 'report_user', 'site', 'department', 'program')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no reports matching the search criteria..."

    def render_edit_link(self, report):
        return mark_safe('<a href=' + reverse("edit", args=[report.pk]) + '>Edit</a>')

    def render_delete_link(self, report):
        return mark_safe('<a href=' + reverse("delete", args=[report.pk]) + '>Delete</a>')

    def get_request_user_id(self, request):
        return self.request.user.id
