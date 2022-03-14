import json
from django.utils.translation import gettext_lazy as _

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.core.exceptions import ValidationError
from collections import Counter

from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
from parler.admin import TranslatableAdmin

from applications.objects import models
from django.forms.models import BaseInlineFormSet

# from django_google_maps import widgets as map_widgets
from applications.objects import widgets as map_widgets
from django_google_maps import fields as map_fields


class RentObjectImageAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    pass


class RentObjectImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.RentObjectImage
    max_num = 100
    extra = 0

    fields = ['image', 'rent_object_photo', 'order']
    readonly_fields = ['rent_object_photo']

    def rent_object_photo(self, obj):
        if obj.pk:
            return format_html('<img src="{url}" height={height} alt="Photo" />',
                               url=obj.image.url,
                               height=70,
                               )
        return _('This will be a preview when you select a file')


class DetailAndFeatureInlineFormset(BaseInlineFormSet):
    def clean(self):
        super(DetailAndFeatureInlineFormset, self).clean()
        list_ = [i[1] for i in Counter([i.cleaned_data['type'].id for i in self.forms]).items() if i[1] > 1]
        if list_:
            raise ValidationError('Types should not be duplicated.')


class DetailAndFeatureInline(admin.TabularInline):
    model = models.DetailAndFeature
    max_num = 10
    extra = 0
    formset = DetailAndFeatureInlineFormset


class RentObjectDocumentAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    pass


class RentObjectDocumentInline(admin.StackedInline):
    model = models.RentObjectDocument
    max_num = 10
    extra = 0


class FloorPlanInline(admin.TabularInline):
    model = models.FloorPlan
    max_num = 10
    extra = 0


class RentObjectReviewInline(admin.TabularInline):
    model = models.RentObjectReview
    max_num = 3
    extra = 0


class RentObjectReservInline(admin.TabularInline):
    model = models.RentObjectReserv
    max_num = 3
    extra = 0


class RentObjectTranslatableAdmin(TranslatableAdmin, SummernoteModelAdmin):

    # inlines = (
    # RentObjectImageInline, RentObjectDocumentInline, FloorPlanInline, DetailAndFeatureInline, RentObjectReviewInline,
    # RentObjectReservInline)

    # filter_horizontal = ['amenities', ]
    # fields_list = [i.name for i in models.RentObject._meta.get_fields() if not i.auto_created]
    # list_display = ['object', 'name']
    # fields = ['object', ] + fields_list
    # readonly_fields = ['object', ]
    # # search_fields = ('category')
    # save_on_top = True
    #
    formfield_overrides = {
        map_fields.AddressField: {'widget':
            map_widgets.GoogleMapsAddressWidgetExt(
                attrs={'data - autocomplete - options':
                    json.dumps({
                        'types': ['geocode', 'establishment'],
                        'componentRestrictions': {'country': 'us'},
                    }),
                    'data-map-type': 'roadmap'
                })
        },
    }
    #
    # @staticmethod
    # def object(obj):
    #     return obj.prim()
    #
    # @staticmethod
    # def get_not_show_field(obj):
    #     return obj.not_show_field


@admin.register(models.Amenity)
class AmenityAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    pass


class DetailAndFeatureAdmin(admin.ModelAdmin):
    pass


class DetailAndFeatureTypeAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        fields = super(DetailAndFeatureTypeAdmin, self).get_fields(request, obj)
        list_attributes = ['Bedrooms', 'Bathrooms', 'Areas', 'Garage', 'Property Type', 'Year', 'Status', 'Cooling',
                           'Heating Type', 'Kitchen Features', 'Swimming Pool', 'Elevator', 'Fireplace', 'Free WiFi']
        for word in list_attributes:
            word_in_base = models.DetailAndFeatureType.objects.filter(name=word)
            if not word_in_base:
                models.DetailAndFeatureType.objects.create(name=word).save()
        return fields


admin.site.register(models.RentObjectDocument, RentObjectDocumentAdmin)
admin.site.register(models.RentObjectImage, RentObjectImageAdmin)

admin.site.register(models.RentObject, RentObjectTranslatableAdmin)

admin.site.register(models.RentObjectReserv, SummernoteModelAdmin)
admin.site.register(models.Category, SummernoteModelAdmin)
admin.site.register(models.RentObjectReview, SummernoteModelAdmin)
admin.site.register(models.DetailAndFeatureType, DetailAndFeatureTypeAdmin)
admin.site.register(models.DetailAndFeature, DetailAndFeatureAdmin)
