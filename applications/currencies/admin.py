from django.contrib import admin
from applications.currencies import models


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass
    # list_display = [i.name for i in models.Currency._meta.get_fields() if i.name != 'object']

