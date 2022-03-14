from django.urls import reverse
from django.db import models
from django.conf import settings
from parler.models import TranslatedFields, TranslatableModel


# class Publication(TranslatableModel):
#     seo_title = models.CharField('Meta title', max_length=100, blank=True)
#     seo_keywords = models.CharField('Meta keywords', max_length=100, blank=True)
#     seo_description = models.CharField('Meta description', max_length=255, blank=True)
#
#     # translations = TranslatedFields(
#     # title = models.CharField('Title', max_length=255, any_language=True)
#     title = models.CharField('Title', max_length=255)
#     # )
#
#     title = models.CharField('Title', max_length=255)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
#     date_created = models.DateField('Date of creation', auto_now_add=True)
#     image = models.ImageField('Picture for the list', null=True, blank=False)
#     image_detail = models.ImageField('Picture for detail', null=True, blank=False)
#     short_description = models.TextField('Short description', blank=True)
#     description = models.TextField('Description', blank=True)
#     viewed = models.PositiveIntegerField('Number of views', default=0)
#
#     class Meta:
#         abstract = True
#
#     def get_absolute_url(self):
#         return reverse(self.url_name, kwargs={'pk': self.pk})
#
#     def __unicode__(self):
#         return self.title


class Blog(TranslatableModel):
    url_name = 'blog'

    translations = TranslatedFields(
        seo_title = models.CharField('Meta title', max_length=100, blank=True),
        seo_keywords = models.CharField('Meta keywords', max_length=100, blank=True),
        seo_description = models.CharField('Meta description', max_length=255, blank=True),
        title = models.CharField('Title', max_length=255),
        short_description = models.TextField('Short description', blank=True),
        description = models.TextField('Description', blank=True),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateField('Date of creation', auto_now_add=True)
    image = models.ImageField('Picture for the list', null=True, blank=False)
    image_detail = models.ImageField('Picture for detail', null=True, blank=False)
    viewed = models.PositiveIntegerField('Number of views', default=0)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def get_absolute_url(self):
        return reverse(self.url_name, kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.title


class Feedbacks(models.Model):

    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email', max_length=20)
    phone = models.CharField('Phone', max_length=20, blank=True)
    image = models.ImageField('Image', upload_to='publications/feedbacks/', null=True, blank=True)
    text = models.TextField('Text')
    date_created = models.DateTimeField('Date of creation', auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
