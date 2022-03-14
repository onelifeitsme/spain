from applications.seo.models import Seo
from django.contrib.flatpages.models import FlatPage


class FlatPageExt(FlatPage, Seo):
    class Meta:
        verbose_name = 'Flat Page Custom'
        verbose_name_plural = 'Flat pages'

