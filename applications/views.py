from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from applications.accounts.forms import SignUpForm
from applications.accounts.models import User
from applications.forms import FeedBackForm
from applications.models import Logo, Address, FeedBack
from applications.objects.models import RentObject, Category
from applications.publications.models import Blog
from applications.search.forms import BaseSearchForm


class IndexView(generic.TemplateView):
    model = User
    template_name = 'index.html'
    form_class = SignUpForm
    success_url = reverse_lazy('/account/login')

    def get_context_data(self, **kwargs):

        context = super(IndexView, self).get_context_data(**kwargs)
        try:
            partners = Logo.objects.all()
            context['partners'] = partners
        except (ObjectDoesNotExist, IndexError):
            context['partners'] = None

        popular_objects = RentObject.objects.filter(popular=True)[:6]
        context['popular_objects'] = popular_objects

        search_form = BaseSearchForm()
        context['search_form'] = search_form

        сategories = Category.objects.all()
        context['сategories'] = сategories

        last_blogs = Blog.objects.all().order_by('-id')[:3]
        context['last_blogs'] = last_blogs

        if self.request.session.get('recent_objects'):
            recent_objects = RentObject.objects.filter(pk__in=self.request.session.get('recent_objects'))
            context['recent_objects'] = recent_objects

        try:
            head_office = Address.objects.get(is_head_office=True)
            context['head_office'] = head_office
        except (ObjectDoesNotExist, IndexError):
            context['head_office'] = None

        return context


class AboutView(generic.TemplateView):
    template_name = 'about_page.html'

    def get_context_data(self, **kwargs):

        context = super(AboutView, self).get_context_data(**kwargs)
        try:
            addresses = Address.objects.all()
            context['addresses'] = addresses
        except (ObjectDoesNotExist, IndexError):
            context['addresses'] = None

        return context


class ContactsView(generic.TemplateView):
    template_name = 'contacts.html'
    model = FeedBack
    form_class = FeedBackForm

    def get_context_data(self, **kwargs):

        context = super(ContactsView, self).get_context_data(**kwargs)
        try:
            head_office = Address.objects.get(is_head_office=True)
            context['head_office'] = head_office
        except (ObjectDoesNotExist, IndexError):
            context['head_office'] = None

        feedback_form = FeedBackForm()
        context['feedback_form'] = feedback_form

        return context

    def post(self, request):
        bound_form = FeedBackForm(request.POST)

        if bound_form.is_valid():
            new_feed_back = bound_form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('/contacts')

        return render(request, 'contacts.html', context={'form': bound_form})
