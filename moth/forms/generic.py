from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class GenericForm(forms.Form):
    text = forms.CharField()
    INPUT = 'text'
    
    def __init__(self, * args, **kwargs):
        # pylint: disable=E1002
        super(GenericForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-x'
        self.helper.field_class = 'col-lg-x'

        submit = Submit('Submit', 'Submit', css_class="btn-success")

        # generate layout
        self.helper.layout = Layout(Field(self.INPUT,),
                                    submit)


class GETGenericForm(GenericForm):

    def __init__(self, * args, **kwargs):
        # pylint: disable=E1002
        super(GETGenericForm, self).__init__(*args, **kwargs)

        self.helper.form_method = 'GET'


class TwoInputForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()

    def __init__(self, * args, **kwargs):
        # pylint: disable=E1002
        super(TwoInputForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-x'
        self.helper.field_class = 'col-lg-x'

        submit = Submit('Submit', 'Submit', css_class="btn-success")

        # generate layout
        self.helper.layout = Layout(Field('name'),
                                    Field('address'),
                                    submit)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, * args, **kwargs):
        # pylint: disable=E1002
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-x'
        self.helper.field_class = 'col-lg-x'

        submit = Submit('Login', 'Login', css_class="btn-success")

        # generate layout
        self.helper.layout = Layout(Field('username'),
                                    Field('password'),
                                    submit)
