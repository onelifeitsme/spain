#!coding:utf-8
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DetailView, ListView, CreateView
from . import models
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Blog


# class QSMixin(object):
#
#     def get_context_data(self, **kwargs):
#         ctx = super(QSMixin, self).get_context_data(**kwargs)
#         # ctx['tags'] = models.Tag.objects.filter(type=self.model.tag_type)
#
#         return ctx
#
#     def get_queryset(self):
#         qs = super(QSMixin, self).get_queryset().order_by('-date_created')
#         tag = self.request.GET.get('tag')
#         if tag:
#             qs = qs.filter(tag__code=tag)
#
#         return qs


class PublicationDetail(DetailView):

    def get_context_data(self, object):
        ctx = super(PublicationDetail, self).get_context_data(object=object)
        object.viewed += 1
        object.save()
        return ctx


# class NewsList(QSMixin, ListView):
#     model = models.News
#     template_name = 'publications/news_list.html'
#
#
#
# class NewsDetail(QSMixin, PublicationDetail):
#     model = models.News
#     template_name = 'publications/news_detail.html'


class BlogList(ListView):
    model = models.Blog
    paginate_by = 9

    template_name = 'publications/blog.html'


class BlogDetail(PublicationDetail):
    model = models.Blog
    template_name = 'publications/blog_detail.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):

        ctx = super(BlogDetail, self).get_context_data(**kwargs)
        try:
            most_viewed_blogs = Blog.objects.all().order_by('-id')[:5]
            ctx['most_viewed_blogs'] = most_viewed_blogs
        except (ObjectDoesNotExist, IndexError):
            ctx['most_viewed_blogs'] = None

        return ctx


class Feedbacks(CreateView):
    model = models.Feedbacks
    fields = ('name', 'email', 'phone', 'image', 'text')
    template_name = 'publications/feedbacks/feedbacks_list.html'
    success_url = reverse_lazy('feedbacks')

    def get_context_data(self, **kwargs):
        ctx = super(Feedbacks, self).get_context_data(**kwargs)
        ctx['object_list'] = models.Feedbacks.objects.all()

        return ctx

    def form_valid(self, form):
        messages.success(self.request, u'Спасибо за ваш отзыв!')
        return super(Feedbacks, self).form_valid(form)