'''
Description - Member Tables
@author - John Sentz
@date - 15-Nov-2018
@time - 7:20 PM
'''

import django_tables2 as tables
from django_tables2 import A

from .models import Member

TEMPLATE_VIEW = '''
       <a href="{% url 'members:detail' record.pk %}">
       <button class="btn btn-primary btn-block"  label="View" name="{% url 'members:detail' record.pk %}">
       <span class="far fa-eye"></span>
       View</button>
       </a>
'''

TEMPLATE_EDIT = '''
       <a href="{% url 'members:member-update' record.pk %}">
       <button class="btn btn-success btn-block"  label="Edit" name="{% url 'members:member-update' record.pk %}">
       <span class="fas fa-pencil-alt"></span>
       Edit</button>
       </a> 
'''

TEMPLATE_DELETE = '''
       <a href="{% url 'members:member-delete' record.pk %}">
       <button class="btn btn-danger btn-block" label="Delete" name="{% url 'members:member-delete' record.pk %}">
       <span class="fas fa-trash-alt"></span>
       Delete</button>
       </a>
   '''

TEMPLATE_EDIT_DISABLED = '''
       <button class="btn btn-success btn-block" disabled  label="Edit" name="{% url 'members:member-update' record.pk %}">
       <span class="fas fa-pencil-alt"></span>
       Edit</button>
'''

TEMPLATE_DELETE_DISABLED = '''
       <button class="btn btn-danger btn-block" disabled label="Delete" name="{% url 'members:member-delete' record.pk %}">
       <span class="fas fa-trash-alt"></span>
       Delete</button>
   '''


class MemberTableLimited(tables.Table):
    age = tables.Column(accessor='get_age', verbose_name='Age', orderable=False)
    view = tables.TemplateColumn(TEMPLATE_VIEW, orderable=False, verbose_name='')
    edit = tables.TemplateColumn(TEMPLATE_EDIT_DISABLED, orderable=False, verbose_name='')
    delete = tables.TemplateColumn(TEMPLATE_DELETE_DISABLED, orderable=False, verbose_name='')

    member_number = tables.LinkColumn('members:detail', args=[A('pk')])
    birth_date = tables.DateColumn(format='j-N-Y')

    class Meta:
        model = Member
        fields = ('member_number', 'first_name', 'last_name', 'gender', 'birth_date')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no members matching the search criteria..."


class MemberTable(tables.Table):
    age = tables.Column(accessor='get_age', verbose_name='Age', orderable=False)
    view = tables.TemplateColumn(TEMPLATE_VIEW, orderable=False, verbose_name='')
    edit = tables.TemplateColumn(TEMPLATE_EDIT, orderable=False, verbose_name='')
    delete = tables.TemplateColumn(TEMPLATE_DELETE, orderable=False, verbose_name='')

    member_number = tables.LinkColumn('members:detail', args=[A('pk')])
    birth_date = tables.DateColumn(format='j-N-Y')

    class Meta:
        model = Member
        fields = ('member_number', 'first_name', 'last_name', 'gender', 'birth_date')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no members matching the search criteria..."


