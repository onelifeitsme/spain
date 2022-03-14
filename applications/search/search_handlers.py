# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import copy
from django.core.paginator import Paginator, InvalidPage
from django.utils.translation import ugettext_lazy as _
from haystack.query import SearchQuerySet

from haystack import connections
from django.conf import settings
# from ..event.models import Event, Place
# from ..organizator.models import Organization
from haystack.forms import SearchForm
# from forms import EventSearchForm, OrganizationSearchForm
from applications.objects.models import RentObject


class SearchHandlerMixin:

    def get_search_results(self, search_form=None):
        return (search_form or self.search_form).search()

    def get_search_form(self, request, request_data, search_queryset, city=None):

        kwargs = {
            'request': request,
            'data': request_data,
            'searchqueryset': search_queryset
        }

        if city:
            kwargs.update({'city': city})

        return self.form_class(**kwargs)

    def get_search_queryset(self):
        sqs = SearchQuerySet()
        if self.model_whitelist:
            sqs = sqs.models(*self.model_whitelist)

        return sqs


class SearchHandler(SearchHandlerMixin):

    model_whitelist = None
    paginate_by = None
    paginator_class = Paginator
    page_kwarg = 'page'

    def __init__(self, request, request_data, full_path, city=None, form_class=None):
        self.full_path = full_path
        self.request_data = request_data
        self.request = request
        self.form_class = form_class or SearchForm

        search_queryset = self.get_search_queryset()

        if city:
            self.search_form = self.get_search_form(
                request, request_data, search_queryset, city)
        else:
            self.search_form = self.get_search_form(
                request, request_data, search_queryset)
        self.results = self.get_search_results(self.search_form)
        self.results_orig = copy.deepcopy(self.results)

        self.paginator, self.page = self.paginate_queryset(
            self.results, request_data)

    def paginate_queryset(self, queryset, request_data):

        paginator = self.get_paginator(queryset)
        page_kwarg = self.page_kwarg
        page = request_data.get(page_kwarg, 1)
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise InvalidPage(_(
                    "Page is not 'last', nor can it be converted to an int."))

        return paginator, paginator.page(page_number)

    def get_paginator(self, queryset):
        return self.paginator_class(queryset, self.paginate_by)

    def bulk_fetch_results(self, paginated_results):

        objects = []

        models_pks = loaded_objects = {}
        for result in paginated_results:
            models_pks.setdefault(result.model, []).append(result.pk)

        search_backend_alias = self.results.query.backend.connection_alias
        for model in models_pks:
            ui = connections[search_backend_alias].get_unified_index()
            index = ui.get_index(model)
            queryset = index.read_queryset(using=search_backend_alias)
            loaded_objects[model] = queryset.in_bulk(models_pks[model])

        for result in paginated_results:
            model_objects = loaded_objects.get(result.model, {})
            try:
                result._object = model_objects[int(result.pk)]
            except KeyError:
                pass
            else:
                objects.append(result._object)

        return objects

    def get_paginated_objects(self):

        if hasattr(self, '_objects'):
            return self._objects
        else:
            #paginated_results = self.page.object_list
            #self._objects = self.bulk_fetch_results(paginated_results)
            page_kwarg = self.page_kwarg
            page = self.request_data.get(page_kwarg, 1)
            try:
                page_number = int(page)
            except ValueError:
                if page == 'last':
                    page_number = self.paginator.num_pages
                else:
                    raise InvalidPage(_(
                        "Page is not 'last', nor can it be converted to an int."))
            queryset = self.results_orig
            start_offset = (page_number - 1) * self.paginate_by
            qs = queryset[start_offset:start_offset + self.paginate_by]

            self._objects = self.bulk_fetch_results(qs)

        return self._objects

    def get_search_context_data(self, context_object_name=None):

        context = {
            'form': self.search_form,
            'paginator': self.paginator,
            'page_obj': self.page,
        }

        if context_object_name is not None:
            context[context_object_name] = self.get_paginated_objects()

        return context


class WhooshEventSearchHandler(SearchHandler):
    model_whitelist = [RentObject]
    # paginate_by = settings.EVENTS_PER_PAGE


