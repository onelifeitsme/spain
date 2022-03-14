from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit, HTML
from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, UsernameField, UserModel, PasswordChangeForm, \
    PasswordResetForm, SetPasswordForm
from django.core.exceptions import ValidationError

from .apps import user_registered
from .models import User
from django import forms


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('avatar', 'full_name', 'email', 'phone', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'signup_form'
        self.helper.form_class = 'form-row'
        self.helper.form_method = 'post'
        self.helper.form_action = '/accounts/profile/'
        self.helper.form_show_labels = False
        self.helper.form_show_errors = True
        # self.helper.help_text_inline = True
        # self.helper.disable_csrf = False
        self.helper.layout = Layout(
            # HTML(
            #     """{% if user_change_form.avatar %}<img class="img-responsive" src="{{ user_change_form.avatar.url }}{{ user_change_form.avatar.url }}">{% endif %}""", ),

            Div(
                HTML("""<label>Email</label>"""),
                Field('email', css_class="form-control", placeholder="Enter Your Email", required=True),
                css_class="form-group col-md-6"),
            Div(
                HTML("""<label>Phone</label>"""),
                Field('phone', css_class="form-control", placeholder="Enter Your Phone"),
                css_class="form-group col-md-6"),
            Div(
                HTML("""<label>Your Full Name</label>"""),
                Field('full_name', css_class="form-control", placeholder="Enter Your Full Name", required=True),
                css_class="form-group col-md-6"),
            Div(
                HTML("""<label>City</label>"""),
                Field('city', css_class="form-control", placeholder="Enter Your City"),
                css_class="form-group col-md-6"),
            Div(
                HTML("""<label>Your Photo</label>"""),
                'avatar',
                HTML('<img src="{{ avatar.url }}" />'),
                HTML("""{% if form.imagefile.value %}<img class="img-responsive" src="{{ MEDIA_URL }}{{ form.imagefile.value }}">{% endif %}""", ),
                # HTML("""<label>Your Photo</label>"""),
                # HTML("""<input type="file" class="form-control-file" id="exampleFormControlFile1">"""),
                # Field('avatar', css_class="form-control", placeholder="Photo"),
                css_class="form-group col-md-6"),
            Div(
                Submit('submit', 'Save Changes', css_class="btn btn-theme bg-2"),
                css_class="form-group col-lg-12 col-md-12 mt-5")
        )


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        # super().__init__(*args, **kwargs)
        #
        # # Set the max length and label for the "username" field.
        # self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        # username_max_length = self.username_field.max_length or 254
        # self.fields['username'].max_length = username_max_length
        # self.fields['username'].widget.attrs['maxlength'] = username_max_length
        # if self.fields['username'].label is None:
        #     self.fields['username'].label = capfirst(self.username_field.verbose_name)

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'login_form'
        self.helper.form_class = 'login-form'
        self.helper.form_method = 'post'
        self.helper.form_action = '/accounts/login/'
        self.helper.form_show_labels = False
        self.helper.form_show_errors = True
        # self.helper.help_text_inline = True
        # self.helper.disable_csrf = False
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        Div(
                            Field('username', css_class="form-control", placeholder="Username"),
                            HTML("""<i class="ti-email"></i>"""),
                            css_class="input-with-icon"),
                        css_class="form-group"),
                    css_class="col-lg-12 col-md-12"),
                Div(
                    Div(
                        Div(
                            Field('password', css_class="form-control", placeholder="Password"),
                            HTML("""<i class="ti-unlock"></i>"""),
                            css_class="input-with-icon"),
                        css_class="form-group"),
                    css_class="col-lg-12 col-md-12"),
                css_class="row"),
            Div(
                Submit('submit', 'Sign In', css_class="btn btn-md full-width pop-login bg-2"),
                css_class="form-group")
        )


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'password1', 'password2')

    full_name = forms.CharField(max_length=100)
    email = forms.EmailField(label="Email", max_length=50)
    password1 = forms.CharField(label='Пароль',
                                # widget=forms.Passwordinput,
                                # help_text=password_validation.password_validators_help_text_html()
                                )
    password2 = forms.CharField(label='Пароль (повторно)',
                                # widget=forms.Passwordinput,
                                # help_text='Введите пароль повторно'
                                )




    @property
    def registred_user(self):
        user = self.save()

        return authenticate(
            username=user.email,
            password=self.cleaned_data.get('password1'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'signup_form'
        self.helper.form_class = 'login-form'
        self.helper.form_method = 'post'
        self.helper.form_show_labels = False
        self.helper.form_show_errors = True
        # self.helper.help_text_inline = True
        # self.helper.disable_csrf = False
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        Div(
                            Field('full_name', css_class="form-control", placeholder="Full Name"),
                            HTML("""<i class="ti-user"></i>"""),
                            css_class="input-with-icon"),
                        css_class="form-group"),
                    css_class="col-lg-12 col-md-12"),
                css_class="row"),
            Div(
                Div(
                    Div(
                        Div(
                            Field('email', css_class="form-control", placeholder="Email"),
                            HTML("""<i class="ti-email"></i>"""),
                            css_class="input-with-icon"),
                        css_class="form-group"),
                    css_class="col-lg-12 col-md-12"),
                css_class="row"),
            Div(
                Div(
                    Div(
                        Div(
                            Field('password1', css_class="form-control", placeholder="Password"),
                            HTML("""<i class="ti-unlock"></i>"""),
                            css_class="input-with-icon"),
                        css_class="form-group"),
                    css_class="col-lg-12 col-md-12"),
                css_class="row"),
            Div(
                Div(
                    Div(
                        Div(
                            Field('password2', css_class="form-control", placeholder="Re-Enter Password"),
                            HTML("""<i class="ti-unlock"></i>"""),
                            css_class="input-with-icon"),
                        css_class="form-group"),
                    css_class="col-lg-12 col-md-12"),
                css_class="row"),
            Div(
                Submit('submit', 'Sign Up', css_class="btn btn-md full-width pop-login bg-2"),
                css_class="form-group")
        )


class CustomPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = None

        self.helper = FormHelper()
        self.helper.form_id = 'password_change_form'
        self.helper.form_class = 'form-row'
        self.helper.form_method = 'post'
        self.helper.form_action = '/accounts/password_change/'
        self.helper.form_show_labels = False
        self.helper.form_show_errors = True
        self.helper.layout = Layout(

            Div(
                HTML("""<label>Old Password</label>"""),
                Field('old_password', css_class="form-control"),
                css_class="form-group col-lg-12 col-md-6"),
            Div(
                HTML("""<label>New Password</label>"""),
                Field('new_password1', css_class="form-control"),
                css_class="form-group col-md-6"),
            Div(
                HTML("""<label>Confirm password</label>"""),
                Field('new_password2', css_class="form-control"),
                css_class="form-group col-md-6"),
            Div(
                Submit('submit', 'Save Changes', css_class="btn btn-theme bg-2"),
                css_class="form-group col-lg-12 col-md-12")
        )


class CustomPasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'password_reset_form'
        self.helper.form_class = 'form-row'
        self.helper.form_method = 'post'
        self.helper.form_action = '/accounts/password_reset/'
        self.helper.form_show_errors = True
        self.helper.layout = Layout(

            Div(
                Div(
                    Div(
                        Field('email', placeholder="Email address used during registration", type="email", css_class="form-control textinput textInput"),
                        css_class="form-group col-lg-12 col-md-6"),
                    css_class="controls"),
                css_class="control-group"),

            Div(
                Submit('submit', 'Send Link', css_class="btn btn-theme bg-2 mt-3"),
                css_class="form-group col-lg-12 col-md-12")
        )


class CustomPasswordResetConfirmForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = None

        self.helper = FormHelper()
        self.helper.form_id = 'password_reset_confirm_form'
        self.helper.form_class = 'form-row'
        self.helper.form_method = 'post'
        self.helper.form_action = '/accounts/reset/<uidb64>/<token>/'
        self.helper.form_show_errors = True
        self.helper.layout = Layout(

            Div(
                Field('new_password1', css_class="form-control"),
                css_class="form-group col-md-6"),
            Div(
                Field('new_password2', css_class="form-control"),
                css_class="form-group col-md-6"),
            Div(
                Submit('submit', 'Set New Password', css_class="btn btn-theme bg-2"),
                css_class="form-group col-lg-12 col-md-12")
        )
