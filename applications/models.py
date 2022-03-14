from django.db import models
from parler.models import TranslatableModel, TranslatedFields
import re


class Logo(models.Model):
    name = models.CharField('Name', max_length=100, blank=True)
    picture = models.ImageField()

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logo'


class AboutUsText(TranslatableModel):
    translations = TranslatedFields(
        text_0=models.TextField(max_length=12000, blank=True)
    )

    class Meta:
        verbose_name = 'About Us Text'
        verbose_name_plural = 'About Us Text'

    def __str__(self):
        return re.sub('<[^>]*>', '', self.text_0)


class AboutUsDetailInformation(TranslatableModel):

    reverse = models.BooleanField(default=False)
    picture = models.ImageField(blank=True)

    translations = TranslatedFields(
        title_1=models.CharField(max_length=200, blank=True),
        subtitle_1=models.CharField(max_length=200, blank=True),
        title_2 = models.CharField(max_length=200, blank=True),
        subtitle_2 = models.CharField(max_length=200, blank=True),
        title_3 = models.CharField(max_length=200, blank=True),
        subtitle_3 = models.CharField(max_length=200, blank=True),
        title_4 = models.CharField(max_length=200, blank=True),
        subtitle_4 = models.CharField(max_length=200, blank=True),
    )

    icon_1 = models.CharField(default='flaticon-beach-house-2', max_length=200, blank=True)
    icon_2 = models.CharField(default='flaticon-apartments', max_length=200, blank=True)
    icon_3 = models.CharField(default='flaticon-student-housing', max_length=200, blank=True)
    icon_4 = models.CharField(default='flaticon-modern-house-4', max_length=200, blank=True)


    class Meta:
        verbose_name = 'About Us Detail Information'
        verbose_name_plural = 'About Us Detail Information'


class Address(models.Model):
    icon_class = models.CharField(default='ti-location-pin', max_length=20)
    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=100, blank=True)
    sub_subtitle = models.CharField(max_length=100, blank=True)
    is_head_office = models.BooleanField(blank=True, null=True)

    def save(self):
        if self.is_head_office == True:
            addresses = Address.objects.filter(is_head_office=True)
            for address in addresses:
                address.is_head_office = False
                address.save()
        super().save()

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class FeedBack(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=150, blank=True, null=True)
    message = models.CharField(max_length=1000, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'
