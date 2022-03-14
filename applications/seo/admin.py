from django.contrib import admin
from . import models


class MainSeoAdmin(admin.ModelAdmin):
    list_display = ['seo_title', 'url']


admin.site.register(models.RegularUrl)
admin.site.register(models.MainSeo, MainSeoAdmin)
