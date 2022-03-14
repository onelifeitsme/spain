from django.db.models import F
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from haystack.generic_views import SearchView

# from accounts.models import Company
# from nsi.models import OKPD2, Decree
# from planning.models import Schedule, PPG
# from purchases.models import NoticeVersion
from .forms import PlanningPublicForm, PurchasePublicForm, BaseSearchForm


# class SchedulePublicListView(SearchView):
#     form_class = BaseSearchForm
#     template_name = 'planning-all.html'
#     ordering = ['-year']
#     context_object_name = 'schedule_list'
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.models(Schedule).all()
#
#
# class SchedulePPGPublicListView(SearchView):
#     form_class = PlanningPublicForm
#     template_name = 'planning-ppg-all.html'
#     ordering = ['-year']
#     context_object_name = 'schedule_ppg_list'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=object_list, **kwargs)
#         context['schedule'] = get_object_or_404(
#             Schedule, pk=self.kwargs.get('pk')
#         )
#         return context
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.models(PPG).filter(schedule_id=self.kwargs.get('pk'))
#
#
# class NoticeVersionPublicListView(SearchView):
#     form_class = PurchasePublicForm
#     template_name = 'purchases-all.html'
#     ordering = ['-pk']
#     context_object_name = 'notice_version_list'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=object_list, **kwargs)
#         context['uo'] = Company.get_uo()
#         return context
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.models(NoticeVersion).filter(status=NoticeVersion.EIS_ACCEPTED)
#
#
# class NoticeVersionPublicDetailView(DetailView):
#     model = NoticeVersion
#     template_name = 'purchase.html'
#
#     def get_queryset(self):
#         return super().get_queryset().with_notice_nmck()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         hierarchy = {}
#         for specification in self.object.specificationnotice_set.all():
#             try:
#                 hierarchy[specification.okpd2.code] = OKPD2.objects \
#                     .select_related(
#                     'parent__parent__parent__parent__parent__parent') \
#                     .get(pk=specification.okpd2.code).hierarchy
#             except OKPD2.DoesNotExist:
#                 pass
#         context['decree_list'] = list(
#             Decree.objects
#                 .exclude(okpd2_exclude__in=hierarchy[x])
#                 .filter(okpd2_include__in=hierarchy[x])
#                 .values(
#                 'name', 'url',
#                 okpd2_code=F('okpd2_include__code'),
#                 okpd2_name=F('okpd2_include__name')
#             ).order_by('name')
#             for x in hierarchy.keys()
#         )
#         return context
