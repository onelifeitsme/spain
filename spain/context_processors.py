from django.contrib.auth.forms import AuthenticationForm

from applications.accounts.forms import SignUpForm, CustomAuthenticationForm
from applications.models import AboutUsText, AboutUsDetailInformation


def about_us_context_processor(request):
    context = {}
    try:
        obj = AboutUsDetailInformation.objects.all()
        context['about_as'] = obj
    except:
        pass

    try:
        obj2 = AboutUsText.objects.all()[0]
        context['about_as_text'] = obj2.text_0
    except:
        pass

    return context


def modal_login_context_processor(request):
    try:
        context = {
            'login_form': CustomAuthenticationForm()
        }
    except:
        context = {}
    return context


def modal_signup_context_processor(request):
    try:
        context = {
            'signup_form': SignUpForm()
        }
    except:
        context = {}
    return context
