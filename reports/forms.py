'''
Description - Reports Forms
@author - John Sentz
@date - 15-Nov-2018
@time - 9:04 PM
'''

from crispy_forms.bootstrap import InlineField, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML
from django import forms
from django.forms import ModelForm
from django_select2 import forms as select2forms

from .models import Member
from .models import Report


class Members(object):
    club_members = Member.objects.all()


class ReportCreateOrUpdateForm(ModelForm):
    class Meta:
        model = Report

        fields = ["report_date",
                  "site",
                  "department",
                  "program",
                  "summary",
                  "feedback_challenges",
                  "members"]

        exclude = ["report_user"]

        widgets = {'site': forms.RadioSelect,
                   'summary': forms.Textarea(attrs={'rows': 4}),
                   'feedback_challenges': forms.Textarea(attrs={'rows': 4}),
                   'members': select2forms.Select2MultipleWidget
                   }


class ReportListFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(ReportListFormHelper, self).__init__(*args, **kwargs)
        InlineField.fields = ''

    class Meta:
        model = Report
        labels = {
            "Date": "report_Date",
            "Site": "site",
            "Department": "department",
            "Program": "program",
            "Summary": "summary",
            "Feedback": "feedback_challenges",
        }

    form_id = 'report-search-form'
    form_class = 'form-inline'
    field_template = 'bootstrap3/layout/inline_field.html'

    form_show_labels = True
    form_show_errors = True
    help_text_inline = False
    html5_required = True
    form_tag = True
    layout = Layout(
        'Staff',
        'Date',
        'Site',
        'Department',
        'Program',

        Fieldset(
            '<i class="fa fa-search"></i>Search Form',

            InlineField('report_user'),
            # InlineField('report_date'),
            InlineField('site'),
            InlineField('department'),
            InlineField('program'),
        ),


        FormActions(
            Submit('search', 'Search', css_class='btn btn-primary'),
            HTML("""
                    <a href="{% url 'reports:report-list'%}">
                        <input type="button" class="btn btn-default" value="Reset">
                    </a>
                """)
        )
    )
