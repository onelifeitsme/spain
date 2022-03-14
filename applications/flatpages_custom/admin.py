from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from applications.flatpages_custom.models import FlatPageExt
from django.contrib.flatpages.admin import FlatPageAdmin


class FlatPageCustomAdmin(FlatPageAdmin):
    fieldsets = ()


admin.site.unregister(FlatPage)
admin.site.register(FlatPageExt, FlatPageCustomAdmin)
