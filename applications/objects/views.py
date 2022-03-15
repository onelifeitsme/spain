import pandas
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, TemplateView
from haystack.generic_views import SearchView
from . import forms
from . import models
from .models import RentObject
from ..search.forms import BaseSearchForm


class RentObjectListView(ListView):
    model = models.RentObject
    paginate_by = 6
    template_name = 'objects/object_list.html'

    def get_queryset(self):
        queryset = models.RentObject.objects.filter(type_of_deal=self.kwargs.get('type_of_deal').upper())
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RentObjectListView, self).get_context_data(**kwargs)
        context['category_set'] = models.Category.objects.filter(
            id__in=context['object_list'].values_list('category_id', flat=True))
        context['form_filter'] = forms.FilterRentObject()
        context['object_list_geo'] = models.RentObject.objects.filter(
            type_of_deal=self.kwargs.get('type_of_deal').upper())
        # if context['object_list']:
        #     context['object_list_area'] = models.RentObject.compute_area(context['object_list'])
        #     context['zoom'] = 3
        return context


class SearchResultRentObjectListView(SearchView):
    model = models.RentObject
    paginate_by = 6
    template_name = 'objects/object_list.html'
    form_class = BaseSearchForm

    def dispatch(self, request, *args, **kwargs):
        dispatch = super().dispatch(request, *args, **kwargs)
        city_object_id = dispatch.context_data['form'].cleaned_data['city']
        city = RentObject.objects.get(id=city_object_id).city
        dispatch.context_data['city'] = city
        # Уничтожить
        object_ids = []
        for object in dispatch.context_data['object_list']:
            object_ids.append(object.pk)
        dispatch.context_data['object_list'] = models.RentObject.objects.filter(id__in=object_ids)
        dispatch.context_data['object_list_geo'] = models.RentObject.objects.filter(
            type_of_deal=dispatch.context_data['object_list'][0].type_of_deal)
        if dispatch.context_data['object_list'] and not dispatch.context_data['city']:
            dispatch.context_data['object_list_area'] = models.RentObject.compute_area(dispatch.context_data['object_list'])
            dispatch.context_data['zoom'] = 3
        # /Уничтожить
        dispatch.context_data['form_filter'] = forms.FilterRentObject()
        return dispatch


class FilterObjectListView(SearchView):
    model = models.RentObject
    paginate_by = 6
    template_name = 'objects/object_list.html'
    form_class = forms.FilterRentObject

    def dispatch(self, request, *args, **kwargs):
        dispatch = super().dispatch(request, *args, **kwargs)
        dispatch.context_data['city'] = dispatch.context_data['form'].cleaned_data['city']
        # Уничтожить
        object_ids = []
        for object in dispatch.context_data['object_list']:
            object_ids.append(object.pk)
        dispatch.context_data['object_list'] = models.RentObject.objects.filter(id__in=object_ids)
        dispatch.context_data['object_list_geo'] = models.RentObject.objects.filter(
            type_of_deal=dispatch.context_data['object_list'][0].type_of_deal)
        if dispatch.context_data['object_list'] and not dispatch.context_data['city']:
            dispatch.context_data['object_list_area'] = models.RentObject.compute_area(dispatch.context_data['object_list'])
            dispatch.context_data['zoom'] = 3
        # /Уничтожить
        dispatch.context_data['form_filter'] = forms.FilterRentObject()
        return dispatch

    def get(self, request, *args, **kwargs):
        get = super(FilterObjectListView, self).get(request, *args, **kwargs)
        return get

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(*, object_list=None, **kwargs)
    #     return context





class FilterByNameObjectListView(SearchView):
    model = models.RentObject
    template_name = 'objects/object_list_for_ajax.html'
    form_class = forms.FilterByNameRentObject

    def form_valid(self, form):
        self.queryset = form.search(type=self.kwargs.get('type_of_deal'))
        context = self.get_context_data(
            **{
                self.form_name: form,
                "query": form.cleaned_data.get(self.search_field),
                "object_list": self.queryset,
            }
        )
        return self.render_to_response(context)


class RentObjectDetailView(DetailView):
    model = models.RentObject
    template_name = 'objects/detail/detail.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RentObjectDetailView, self).get_context_data(**kwargs)
        context['detailandfeatures'] = models.DetailAndFeature.objects.filter(rent_object=context['object'])
        context['floors'] = context['object'].floorplan_set.all()
        context['images'] = context['object'].rentobjectimage_set.all()
        if self.request.user.is_authenticated:
            context['reviews'] = context['object'].rentobjectreview_set.filter(Q(user=self.request.user) |
                                                                               Q(pre_moderation=True)).order_by(
                '-create_date')[:3]
            context['reviews_count'] = context['object'].rentobjectreview_set.filter(Q(user=self.request.user) |
                                                                                     Q(pre_moderation=True)).count
        else:
            context['reviews'] = context['object'].rentobjectreview_set.filter(pre_moderation=True).order_by(
                '-create_date')[:3]
            context['reviews_count'] = context['object'].rentobjectreview_set.filter(pre_moderation=True).count
        context['form_review'] = forms.ReviewForm()
        context['form_reserv'] = forms.ReservForm()

        context['users_who_added'] = context['object'].favorites.all()

        if self.request.is_ajax():
            self.get_reserved_date_list(context['object'].rentobjectreserv_set.all())
            return context
        return context

    def get_object(self):
        obj = super().get_object()
        obj.rent_object_view_count += 1
        obj.save()

        return obj

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')

        if self.request.session.get("recent_objects") and pk:
            if pk not in self.request.session["recent_objects"][-3:]:
                self.request.session["recent_objects"].append(pk)

        elif pk:
            self.request.session["recent_objects"] = [pk]
        request.session.modified = True

        if request.is_ajax():
            response = self.get_reserved_date_list(models.RentObject.objects.get(pk=kwargs.get('pk'))
                                                   .rentobjectreserv_set.all())
            return JsonResponse(response)
        return super().get(request, *args, **kwargs)

    @staticmethod
    def get_reserved_date_list(queryset):
        date_list = {}
        for reserv in queryset:
            dates = pandas.date_range(reserv.checkin, reserv.checkout, freq='d')
            for timestamp in dates:
                date_list.setdefault(timestamp.date().strftime('%Y-%m-%d'), True)
        return date_list


class AddReview(CreateView):
    form_class = forms.ReviewForm
    model = models.RentObjectReview

    def dispatch(self, request, *args, **kwargs):
        self.parent_object = get_object_or_404(models.RentObject, pk=self.kwargs.get('pk'))
        self.user = request.user
        dispatch = super().dispatch(request, *args, **kwargs)
        return dispatch

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.rent_object = self.parent_object
        self.object.user = self.user
        self.object.save()
        if self.request.is_ajax():
            #     data = {
            #         'object': {
            #             'id': self.object.id,
            #             'message': self.object.text,
            #             'user_name': self.object.user_name,
            #             'title': self.object.title,
            #             'email': self.object.email,
            #         }
            #     }
            return JsonResponse({'success': True})
        else:
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('object_detail', kwargs={'pk': self.parent_object.pk})


class ReviewRender(TemplateView):
    template_name = 'objects/detail/comment_list.html'

    def dispatch(self, request, *args, **kwargs):
        self.parent_object = get_object_or_404(models.RentObject, pk=self.kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(ReviewRender, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['reviews'] = self.parent_object.rentobjectreview_set.filter(Q(user=self.request.user) |
                                                                                Q(pre_moderation=True)).order_by(
                '-create_date')[:3]
            context['reviews_count'] = self.parent_object.rentobjectreview_set.filter(Q(user=self.request.user) |
                                                                                      Q(pre_moderation=True)).count
        return context


class AddReserv(CreateView):
    form_class = forms.ReservForm



    def dispatch(self, request, *args, **kwargs):
        self.parent_object = get_object_or_404(models.RentObject, pk=self.kwargs.get('pk'))
        self.user = request.user
        dispatch = super().dispatch(request, *args, **kwargs)
        return dispatch

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.rent_object = self.parent_object
        self.object.user = self.user

        reserved_date = models.RentObjectReserv.objects.exclude(pk=self.object.pk).filter(
            Q(checkin__range=(self.object.checkin, self.object.checkout)) |
            Q(checkout__range=(self.object.checkin, self.object.checkout)) |
            Q(checkin__gte=self.object.checkin, checkout__lte=self.object.checkout) |
            Q(checkin__lte=self.object.checkin, checkout__gte=self.object.checkout))
        if not reserved_date.exists() and self.object.checkin <= self.object.checkout:
            self.object.save()
            if self.request.is_ajax():
                return JsonResponse({
                    'success': True,
                    'checkin': self.object.checkin,
                    'checkout': self.object.checkout,
                })
        else:
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('object_detail', kwargs={'pk': self.parent_object.pk})
