from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Field, Submit
from django import forms

from applications.models import FeedBack


class FeedBackForm(forms.Form):
    class Meta:
        model = FeedBack
        fields = ['name', 'email', 'subject', 'message']

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=150)
    message = forms.CharField(max_length=1000)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'feedback_form'
        self.helper.form_class = 'form-simple'
        self.helper.form_method = 'post'
        # self.helper.form_action = 'send_feedback/'
        self.helper.form_show_labels = True
        # self.helper.disable_csrf = False
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        Field('name', css_class='form-control simple', placeholder="Name"),
                        css_class='form-group'),
                    css_class='col-lg-6 col-md-12'),
                Div(
                    Div(
                        Field('email', css_class='form-control simple', placeholder="Email"),
                        css_class='form-group'),
                    css_class='col-lg-6 col-md-12'),
                css_class="row"),
            Div(
                Div(
                    Field('subject', css_class='form-control simple', placeholder="Subject"),
                    css_class='input-with-icon'),
                css_class='form-group'),
            Div(
                Div(
                    Field('message', css_class='form-control simple', placeholder="Message"),
                    css_class='input-with-icon'),
                css_class='form-group none'),
            Div(
                Submit('submit', 'Submit Request', css_class='btn btn-theme bg-2'),
                css_class='form-group'),

        )

    def save(self):
        new_feed_back = FeedBack.objects.create(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            subject=self.cleaned_data['subject'],
            message=self.cleaned_data['message'],
        )
        return new_feed_back
