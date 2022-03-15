import datetime

from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.signing import BadSignature
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic
from django.views.generic import ListView
from django.views.generic.detail import BaseDetailView
from django.views.generic.edit import CreateView, UpdateView

from .forms import SignUpForm, CustomUserChangeForm, CustomAuthenticationForm, CustomPasswordChangeForm, \
    CustomPasswordResetForm, CustomPasswordResetConfirmForm
from .models import User
from .utilities import signer
from ..objects.models import RentObject, RentObjectReserv


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm

    def get_context_data(self, **kwargs):
        context = super(CustomPasswordChangeView, self).get_context_data(**kwargs)
        user = self.request.user
        password_change_form = CustomPasswordChangeForm(user)
        context['password_change_form'] = password_change_form
        return context


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm

    def get_context_data(self, **kwargs):
        context = super(CustomPasswordResetView, self).get_context_data(**kwargs)
        # user = self.request.user
        password_reset_form = CustomPasswordResetForm()
        context['password_reset_form'] = password_reset_form

        return context


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordResetConfirmForm

    def get_context_data(self, **kwargs):
        # kwargs['user'] = self.user
        context = super(CustomPasswordResetConfirmView, self).get_context_data(**kwargs)
        user = self.request.user
        password_reset_confirm_form = CustomPasswordResetConfirmForm(user)
        context['password_reset_confirm_form'] = password_reset_confirm_form

        return context

class RegisterUserView(CreateView):
    template_name = 'registration/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    #
    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.cleaned_data)
        return super().post(self, request, *args, **kwargs)



class UserProfileView(generic.TemplateView):
    model = User
    template_name = 'registration/profile.html'
    form_class = CustomUserChangeForm


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/profile_change.html'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile')
    success_message = 'User data changed'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

    def get_context_data(self, **kwargs):
        context = super(ChangeUserInfoView, self).get_context_data(**kwargs)
        user = User.objects.get(id=self.user_id)
        data = {
            'avatar': user.avatar,
            'email': user.email,
            'full_name': user.full_name,
            'phone': user.phone,
            'city': user.city,
        }
        user_change_form = CustomUserChangeForm(initial=data)
        context['user_change_form'] = user_change_form

        return context


def user_activate(request, sign):
    try:
        email = signer.unsign(sign)
    except BadSignature:
        return render(request, 'registration/bad_signature.html')
    user = get_object_or_404(User, email=email)
    if user.is_active:
        # if user.is_activated:
        template = 'registration/user_is_activated.html'
    else:
        template = 'registration/activation_done.html'
        user.is_active = True
        # user.is_activated = True
        user.save()
    return render(request, template)


class FavoriteRemove(BaseDetailView):
    model = RentObject

    def get(self, request, *args, **kwargs):
        rent_object = get_object_or_404(RentObject, id=kwargs.get('id'))
        if rent_object.favorites.filter(id=request.user.id).exists():
            rent_object.favorites.remove(request.user.id)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


class FavoriteGet(BaseDetailView):
    model = RentObject

    def get(self, request, *args, **kwargs):
        rent_object = get_object_or_404(RentObject, id=kwargs.get('id'))
        if rent_object.favorites.filter(id=request.user.id).exists():
            return JsonResponse({'in_favorites': True})
        return JsonResponse({'in_favorites': False})


class FavoriteAdd(BaseDetailView):
    model = RentObject

    def get(self, request, *args, **kwargs):

        rent_object = get_object_or_404(RentObject, id=kwargs.get('id'))
        if rent_object.favorites.filter(id=request.user.id).exists():
            rent_object.favorites.remove(request.user.id)
        else:
            rent_object.favorites.add(request.user.id)

        return JsonResponse({'Success': True})


class RentStatusGet(BaseDetailView):
    model = RentObjectReserv

    def get(self, request, *args, **kwargs):
        rent_object_reserv = get_object_or_404(RentObjectReserv, id=kwargs.get('id'))
        if rent_object_reserv:
            today = datetime.datetime.now().date()
            if rent_object_reserv.checkout < today:
                return JsonResponse({'rent_status': 'Paused', 'class': ''})
            elif rent_object_reserv.checkout == today:
                return JsonResponse({'rent_status': '< 24h', 'class': 'expire'})
            elif rent_object_reserv.checkout <= today + datetime.timedelta(days=3):
                return JsonResponse({'rent_status': f'from {rent_object_reserv.checkin} '
                                                    f'to {rent_object_reserv.checkout}',
                                     'class': 'attention'})
            else:
                return JsonResponse({'rent_status': f'from {rent_object_reserv.checkin} '
                                                    f'to {rent_object_reserv.checkout}',
                                     'class': 'published'})

        return JsonResponse({'in_favorites': False})


class HistoryRentObjectListView(ListView):
    model = RentObject
    paginate_by = 6
    template_name = 'accounts/history.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HistoryRentObjectListView, self).get_context_data(**kwargs)
        try:
            # all_rent_object_reserv = RentObjectReserv.objects.filter(user=self.request.user)
            context['history_reserves'] = RentObjectReserv.objects.filter(user=self.request.user)
        except (ObjectDoesNotExist, IndexError):
            context['history_reserves'] = None

        return context


class FavoriteRentObjectListView(ListView):
    model = RentObject
    paginate_by = 6
    template_name = 'accounts/favorite_rent_object_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FavoriteRentObjectListView, self).get_context_data(**kwargs)
        try:
            rent_objects = RentObject.objects.all()
            context['favorite_rent_objects'] = rent_objects.filter(favorites=self.request.user)
        except (ObjectDoesNotExist, IndexError):
            context['favorite_rent_objects'] = None
        return context
