from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from parler.admin import TranslatableAdmin

from applications.models import Logo, AboutUsText, Address, FeedBack, AboutUsDetailInformation


class AboutUsTextTranslatableAdmin(TranslatableAdmin, SummernoteModelAdmin):
    pass
    # list_display = ('text_0',)
    # fieldsets = (
    #     (None, {
    #         'fields': ('text_0',),
    #     }),
    # )


class AboutUsDetailInformationTranslatableAdmin(TranslatableAdmin, SummernoteModelAdmin):
    pass
    # model = AboutUsDetailInformation


admin.site.register(Logo, SummernoteModelAdmin)
admin.site.register(AboutUsText, AboutUsTextTranslatableAdmin)

admin.site.register(AboutUsDetailInformation, AboutUsDetailInformationTranslatableAdmin)
admin.site.register(Address, SummernoteModelAdmin)
admin.site.register(FeedBack, SummernoteModelAdmin,)
