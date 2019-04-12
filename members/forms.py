'''
Description - Member Forms
@author - John Sentz
@date - 15-Nov-2018
@time - 7:12 PM
'''
from crispy_forms.bootstrap import FormActions, InlineField
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Fieldset, Submit, HTML
from datetime import date
from django import forms
from django.forms import ModelForm
from django.urls import reverse

from members.models import Member

GENDER_CHOICES = ((0, 'Girl',), (1, 'Boy',))


class MemberCreateOrUpdateForm(ModelForm):

    class Meta:
        model = Member
        fields = ['member_number',
                  'first_name',
                  'last_name',
                  'gender',
                  'birth_date']

        widgets = {'gender': forms.RadioSelect}

    def clean_birth_date(self):

        today = date.today()
        birth_date = self.cleaned_data.get("birth_date")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        if age < 6 or age > 18:
            raise forms.ValidationError("Member age must fall in the range 6 to 18")
        return birth_date


class StrictButton2(object):
    pass


class MemberListFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(MemberListFormHelper, self).__init__(*args, **kwargs)
        InlineField.fields = ''

    class Meta:
        model = Member

    labels = {
        "MEMBER ID": "member_number",
        "LAST": "last_name",
    }

    form_id = 'member-search-form'
    form_class = 'form-inline'
    field_template = 'bootstrap3/layout/inline_field.html'

    form_show_labels = True
    form_show_errors = True
    help_text_inline = False
    html5_required = True
    form_tag = True

    layout = Layout(
        Fieldset(
            '<i class="fas fa-search"></i>Search Form',
            InlineField('member_number'),
            InlineField('last_name'),
            InlineField('gender'),

        ),
        FormActions(
            Submit('search', 'Search', css_class='btn btn-primary'),
            HTML("""
                <a href="{% url 'members:member-list'%}">
                    <input type="button" class="btn btn-default" value="Reset">
                </a>
            """)
        )
    )

