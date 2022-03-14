from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils.safestring import mark_safe
from parler.models import TranslatedFields, TranslatableModel

from applications.currencies.models import *
from applications.seo.models import *

from django_google_maps import fields as map_fields
from PIL import Image


class Amenity(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    code = models.CharField(verbose_name='Code', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'


class FloorPlan(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    areas = models.FloatField('Areas', default=0)

    FEET = 'ft'
    METER = 'm'
    UOM_CHOICES = [
        (FEET, 'sq ft'),
        (METER, 'sq m'),
    ]

    uom = models.CharField(choices=UOM_CHOICES, verbose_name='Unit of Measures', max_length=6, default=FEET)
    attachment = models.FileField('Attachment')
    rent_object = models.ForeignKey('RentObject', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Category(Seo):
    name = models.CharField(verbose_name='Name', max_length=255)
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class RentObject(TranslatableModel):

    primary_image = models.ImageField(upload_to='images', null=True)

    translations = TranslatedFields(
        seo_title=models.CharField('Meta title', max_length=100, blank=True, null=True),
        seo_keywords=models.CharField('Meta keywords', max_length=100, blank=True, null=True),
        seo_description=models.TextField('Meta description', max_length=255, blank=True, null=True),
        name=models.CharField(verbose_name='Name', max_length=255, default="New", null=True),
        text=models.TextField(verbose_name='Text', blank=True, null=True),
        hidden_details=models.CharField('Hidden details', max_length=255, blank=True, null=True),
    )
    NIGHT = 'Per Night'
    WEEK = 'Per Week'
    MONTH = 'Per Month'
    TYPE_RENT_PERIOD = [
        (NIGHT, _('Per Night')),
        (WEEK, _('Per Week')),
        (MONTH, _('Per Month')),
    ]
    type_rent_period = models.CharField(max_length=10, choices=TYPE_RENT_PERIOD, default=NIGHT, blank=True, null=True)
    RENT = 'RENT'
    SALE = 'SALE'
    TYPE_OF_DEAL_CHOICES = [
        (RENT, _('Rent')),
        (SALE, _('Sale')),
    ]
    type_of_deal = models.CharField(max_length=4, choices=TYPE_OF_DEAL_CHOICES, verbose_name='Type of deal', null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField('Price', null=True, blank=True, default=0)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    popular = models.BooleanField('Popular', blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    attachment = models.FileField(upload_to='documents', null=True, blank=True)
    rent_object_view_count = models.IntegerField(default=0)

    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite', default=None, blank=True)

    address = map_fields.AddressField(max_length=200, null=True)
    geolocation = map_fields.GeoLocationField(max_length=100, null=True)

    def __str__(self):
        if not self.name:
            self.name = "New"
        return self.name

    @staticmethod
    def get_all_cities():
        cities = {}
        try:
            rent_objects = RentObject.objects.all()
            for rent_object in rent_objects:
                if rent_object.city:
                    cities.setdefault((rent_object.city, rent_object.city))
        except:
            pass
        return list(cities)

    @staticmethod
    def get_all_amenities():
        amenities_dict = {}
        try:
            amenities = Amenity.objects.all()
            for am in amenities:
                amenities_dict.setdefault((am.id, am.name))
        except:
            pass
        return list(amenities_dict)

    @staticmethod
    def get_all_details_and_features():
        details_and_features_dict = {}
        try:
            details_and_features = DetailAndFeatureType.objects.all()
            for el in details_and_features:
                details_and_features_dict.setdefault((el.id, el.name))
        except:
            pass
        return list(details_and_features_dict)

    @staticmethod
    def get_all_bedrooms():
        amenities_dict = {}
        amenities = Amenity.objects.all()
        for am in amenities:
            amenities_dict.setdefault((am.id, am.name))
        return list(amenities_dict)

    def get_avatar(self):
        if not self.primary_image:
            return '/media/images/empty.png'
        return self.primary_image.url

    # method to create a fake table field in read only mode
    def prim(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_avatar())

    prim.short_description = 'Primary image'

    @staticmethod
    def compute_area(object_list):
        geo_locations = [i.geolocation for i in object_list if i.geolocation]
        lat = 0.0
        lon = 0.0
        divisor = len(geo_locations)
        for loc in geo_locations:
            lat += loc.lat
            lon += loc.lon

        return {'lat': lat / divisor, 'lng': lon / divisor}


class RentObjectImage(models.Model):
    image = models.ImageField(upload_to='images')
    rent_object = models.ForeignKey(RentObject, on_delete=models.CASCADE)
    order = models.IntegerField(
        default=0,
        db_index=True,
        verbose_name='Display order'
    )

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 1080 or img.width > 1920:
            new_img = (1920, 1080)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving ima

    # def __str__(self):
    #     return self.image.name.split('/')[1]
    def __str__(self):
        rent_obj = self.rent_object.name
        ordering_number = self.order
        return f"{ordering_number} Photo of - {rent_obj}"

    class Meta:
        ordering = ['order']
        verbose_name = 'Image'


class RentObjectDocument(models.Model):
    file = models.FileField(upload_to='documents')
    rent_object = models.ForeignKey(RentObject, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name.split('/')[1]

    class Meta:
        verbose_name = 'Document'


class DetailAndFeature(models.Model):
    type = models.ForeignKey('DetailAndFeatureType', on_delete=models.CASCADE, null=True)
    property = models.CharField(max_length=255, default='-')
    rent_object = models.ForeignKey(RentObject, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.type.name

    class Meta:
        verbose_name_plural = 'Details And Features'


class DetailAndFeatureType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RentObjectReserv(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    checkin = models.DateField(verbose_name=_('Check In'))
    checkout = models.DateField(verbose_name=_('Check Out'))
    adults = models.IntegerField(verbose_name=_('Adults'), null=True, blank=True)
    kids = models.IntegerField(verbose_name=_('Kids'), null=True, blank=True)
    total_price = models.IntegerField(verbose_name=_('Total'), null=True, blank=True)
    rent_object = models.ForeignKey(RentObject, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=True)
    animals = models.BooleanField(verbose_name=_('With pets'), default=False)

    def __str__(self):
        return f'from {self.checkin} to {self.checkout} created ' \
               f'"{self.create_date.strftime("%d/%m/%Y %H:%M")}" by {self.user}'

    class Meta:
        ordering = ['-create_date']


class RentObjectReview(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    # email = models.EmailField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    # user_name = models.CharField(max_length=255, null=True)
    rent_object = models.ForeignKey(RentObject, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    pre_moderation = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} - object "{self.rent_object}"'
