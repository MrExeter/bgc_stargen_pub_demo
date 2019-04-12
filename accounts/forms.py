from crispy_forms.bootstrap import FormActions, StrictButton, InlineField
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Fieldset, Submit, Reset, Button, HTML
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        model = User

    # Make sure email is unique as is the username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses already in use.')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "First"
        self.fields['last_name'].label = "Last"
        self.fields['username'].label = 'Username'
        self.fields['email'].label = "Email Address"


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserListFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(UserListFormHelper, self).__init__(*args, **kwargs)
        # InlineField.fields = ''

    form_id = 'user_list_form'
    form_class = 'form-inline'
    field_template = 'bootstrap3/layout/inline_field.html'
    # field_class = 'col-xs-3'
    # label_class = 'col-xs-3'
    form_show_errors = True
    help_text_inline = False
    html5_required = True

    layout = Layout(
        Fieldset(
            '<i class="fa fa-search"></i> Search Staff Records',
            InlineField('first_name'),
            InlineField('last_name'),
            InlineField('username'),
            InlineField('email'),

        ),
        FormActions(
            Submit('search', 'Search', css_class='btn btn-primary'),
            HTML("""
                    <a href="{% url 'accounts:user-list'%}">
                        <input type="button" class="btn btn-default" value="Reset">
                    </a>
                """)
        )
    )
