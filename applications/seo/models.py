from django.db import models
from django.contrib.flatpages.models import FlatPage

class RegularUrl(models.Model):
    url = models.CharField('Url', max_length=200)

    def __str__(self):
        return self.url


class Seo(models.Model):
    seo_title = models.CharField('Meta title', max_length=100, blank=True)
    seo_keywords = models.CharField('Meta keywords', max_length=100, blank=True)
    seo_description = models.TextField('Meta description', max_length=255, blank=True)


    class Meta:
        abstract = True


class MainSeo(Seo):
    seo_text = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=2100, null=True, blank=True)


    class Meta:
        verbose_name = 'Seo'
        verbose_name_plural = 'Seo'
        ordering = ('url',)


    def __unicode__(self):
        return u'{}: {}'.format(self.url, self.seo_title)

    @staticmethod
    def as_dict(obj):
        return {'title': obj.seo_title, 'keywords': obj.seo_keywords,
                'description': obj.seo_description}

    @classmethod
    def get_nearest(cls, url):
        for path in cls.reductor(url):
            try:
                return cls.objects.filter(url=path).first()
            except:
                pass

    @staticmethod
    def reductor(url):
        tokens = url.split('/')[1:]
        while tokens:
            tokens.pop()
            yield '/'.join([''] + tokens + [''])

