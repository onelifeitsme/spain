from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from parler.admin import TranslatableAdmin

from . import models



class PublicationTranslatableAdmin(TranslatableAdmin, SummernoteModelAdmin):
    list_display = ['title', 'date_created', 'viewed']

    def get_form(self, request, obj=None, **kwargs):
        form = super(PublicationTranslatableAdmin, self).get_form(request, obj, **kwargs)
        # form.base_fields['tag'].queryset = models.Tag.objects.filter(type=self.model.tag_type)
        return form


# admin.site.register(models.News, PublicationAdmin)
admin.site.register(models.Blog, PublicationTranslatableAdmin)
admin.site.register(models.Feedbacks, SummernoteModelAdmin)
