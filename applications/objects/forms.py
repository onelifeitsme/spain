from django.utils.translation import gettext_lazy as _
from crispy_forms.bootstrap import InlineRadios
from django import forms
from django.forms.widgets import ChoiceWidget

from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Field, Div, BaseInput, ButtonHolder, Fieldset
from haystack.forms import SearchForm
from django.db.models import Q


class ReviewForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'text']
        model = models.RentObjectReview

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'review_form'
        self.helper.form_class = 'form-simple'
        self.helper.form_method = 'post'
        self.helper.form_action = 'review/'
        self.helper.form_show_labels = False
        self.helper.disable_csrf = False
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        Field('text', css_class='form-control ht-80', placeholder="Messages"),
                        css_class='form-group'),
                    css_class='col-lg-12 col-md-12 col-sm-12'),
                Div(
                    Div(
                        Field('title', css_class='form-control', placeholder="Property Title"),
                        css_class='form-group'),
                    css_class='col-lg-12 col-md-12 col-sm-12'),

                # Div(
                #     Div(
                #         Field('user_name', css_class='form-control', placeholder="Your Name"),
                #         css_class='form-group'),
                #     css_class='col-lg-6 col-md-6 col-sm-12'),
                #
                # Div(
                #     Div(
                #         Field('email', css_class='form-control', placeholder="Your Email"),
                #         css_class='form-group'),
                #     css_class='col-lg-6 col-md-6 col-sm-12'),
                Div(
                    Div(
                        Submit('submit', 'Submit Review', css_class='btn btn-theme sub'),
                        css_class='form-group'),
                    css_class='col-lg-6 col-md-6 col-sm-12'),
                css_class="row"),
        )


class ReservForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = models.RentObjectReserv

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'reserv_form'
        self.helper.form_class = 'side-booking-body'
        self.helper.form_method = 'post'
        self.helper.form_action = 'reserved/'
        self.helper.form_show_labels = False
        self.helper.disable_csrf = False

        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        Div(HTML('<i class="ti-calendar"></i>'),
                            Field('checkin', wrapper_class='form_reserv_field', type="text", autocomplete="off", css_class='form-control',
                                  placeholder=_('Check In')),
                            css_class='cld-box'), css_class='form-group'),
                    css_class='col-lg-12 col-md-12 col-sm-6'),
                Div(
                    Div(
                        Div(HTML('<i class="ti-calendar"></i>'),
                            Field('checkout', wrapper_class='form_reserv_field', type="text", autocomplete="off", css_class='form-control',
                                  placeholder=_('Check Out')),
                            css_class='cld-box'), css_class='form-group'),
                    css_class='col-lg-12 col-md-12 col-sm-6'),
                Div(
                    Div(
                        Div(HTML(f'<label for="guests">{_("Adults")}</label>'),
                            Div(
                            HTML('<button class="counter-btn" type="button" id="cnt-down"><i class="ti-minus"></i></button>'),
                                BaseInput('adults', type="text", css_id="guestNo", value="0"),
                            HTML('<button class="counter-btn" type="button" id="cnt-up"><i class="ti-plus"></i></button>'), css_class='guests-box'),
                            css_class='guests'), css_class='form-group'),
                    css_class='col-lg-6 col-md-6 col-sm-6 col-6'),
                Div(
                    Div(
                        Div(HTML(f'<label for="guests">{_("Kids")}</label>'),
                            Div(
                            HTML('<button class="counter-btn" type="button" id="kcnt-down"><i class="ti-minus"></i></button>'),
                            BaseInput('kids', type="text", css_id="kidsNo", value="0"),
                            HTML('<button class="counter-btn" type="button" id="kcnt-up"><i class="ti-plus"></i></button>'), css_class='guests-box'),
                            css_class='guests'), css_class='form-group'),
                    css_class='col-lg-6 col-md-6 col-sm-6 col-6'),
                Div(
                    Div(
                        HTML(f'<label for="id_animals" class="">{_("With pets")}</label>'),
                        Field('animals', type="checkbox", css_class='form-check-input ml-2')
                        , css_class='form-group d-flex'),
                    css_class='col-lg-6 col-md-6 col-sm-6 col-6'),
                Field('total_price', type='hidden', step="0.01", css_id="price", css_class="price theme-cl", value="0"),
                HTML(f'<div class="side-booking-foot"><span class="sb-header-left">{_("Total")}</span><h3 class="price theme-cl">'+'{{object.currency.symbol}} <span class="total_price">0</span></h3></div>'),
                Div(
                    Div(
                        Div(
                            Div(
                                ButtonHolder(
                                    Submit('submit', _('Book It Now'), css_class='btn btn-md full-width btn-theme bg-2')
                                )
                                ,
                            ), css_class='form-group mb-0 pb-0'
                        ), css_class='stbooking-footer mt-1')
                , css_class='col-lg-12 col-md-12 col-sm-12'),
                css_class="row"),
        )


class RadioSelectFilter(ChoiceWidget):
    input_type = 'radio'
    template_name = 'django/forms/widgets/radio_custom.html'
    option_template_name = 'django/forms/widgets/input_option_custom.html'


class FilterRentObject(SearchForm):
    city = forms.ChoiceField(
        required=False,
        # label='WHERE',
        choices=[("", _("All"))] + models.RentObject.get_all_cities(),
        widget=RadioSelectFilter())
    property_types = forms.ChoiceField(
        required=False,
        choices=[("", _("All"))] + models.RentObject.get_all_details_and_features(),
        widget=RadioSelectFilter())
    bedrooms = forms.ChoiceField(
        required=False,
        choices=[("", _("All")),
                 ('1', f'01 {_("Bedroom")}'),
                 ('2', f'02 {_("Bedroom")}'),
                 ('3', f'03 {_("Bedroom")}'),
                 ('4', f'04 {_("Bedroom")}'),
                 ('5', f'05 {_("Bedroom")}'),
                 ('6', f'06+ {_("Bedroom")}'),
                 ],
        widget=RadioSelectFilter())
    price_range = forms.ChoiceField(
        required=False,
        choices=[("", _('All')),
                 ("0,1000", _('Less Then €1,000')),
                 ("1000,2000", '€1,000 - €2,000'),
                 ("2000,4000", '€2,000 - €4,000'),
                 ("4000,8000", '€4,000 - €8,000'),
                 ("8000,15000", '€8,000 - €15,000'),
                 ],
        widget=RadioSelectFilter())
    amenities = forms.ChoiceField(
        required=False,
        choices=[("", _('All'))] + models.RentObject.get_all_amenities(),
        widget=RadioSelectFilter())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_id = 'review_formsdfs'
        self.helper.form_class = 'filter-list'
        self.helper.form_method = 'get'
        self.helper.form_action = 'filter_rent_object'
        self.helper.form_show_labels = True
        self.helper.disable_csrf = False
        self.helper.use_custom_control = True
        self.helper.layout = Layout(
            Div(
                Div(HTML(f'<h4><a href="#city" data-toggle="collapse" aria-expanded="false" role="button" class="collapsed">{_("Where")}<span class="selected">{_("Make your choice")}</span></a></h4>')
                    , css_class='widget-boxed-header'),
                Div(
                    Div(
                        Div(
                            Div(
                                Div(
                                    Field('city', css_class='radio-custom',
                                          template="crispy/object_list_filter.html",
                                          wrapper_class='no-ul-list filter-list'),
                                    css_class='inner_widget_link'),
                                css_class='card-body pt-0'),
                            css_class='single_filter_card'),
                        css_class='side-list no-border'),
                css_class="widget-boxed-body collapse", css_id='city'),
            css_class="single_search_boxed"),
            Div(
                Div(HTML(f'<h4><a href="#property_types" data-toggle="collapse" aria-expanded="false" role="button" class="collapsed">{_("property types")}<span class="selected">{_("Make your choice")}</span></a></h4>')
                    , css_class='widget-boxed-header'),
                Div(
                    Div(
                        Div(
                            Div(
                                Div(
                                    Field('property_types', css_class='radio-custom',
                                          template="crispy/object_list_filter.html",
                                          wrapper_class='no-ul-list filter-list'),
                                    css_class='inner_widget_link'),
                                css_class='card-body pt-0'),
                            css_class='single_filter_card'),
                        css_class='side-list no-border'),
                css_class="widget-boxed-body collapse", css_id='property_types'),
            css_class="single_search_boxed"),
            Div(
                Div(HTML(f'<h4><a href="#bedrooms-filter" data-toggle="collapse" aria-expanded="false" role="button" class="collapsed">{_("bedrooms")}<span class="selected">{_("Make your choice")}</span></a></h4>')
                    , css_class='widget-boxed-header'),
                Div(
                    Div(
                        Div(
                            Div(
                                Div(
                                    Field('bedrooms', css_class='radio-custom',
                                          template="crispy/object_list_filter.html",
                                          wrapper_class='no-ul-list filter-list'),
                                    css_class='inner_widget_link'),
                                css_class='card-body pt-0'),
                            css_class='single_filter_card'),
                        css_class='side-list no-border'),
                css_class="widget-boxed-body collapse", css_id='bedrooms-filter'),
            css_class="single_search_boxed"),
            Div(
                Div(HTML(f'<h4><a href="#price_range" data-toggle="collapse" aria-expanded="false" role="button" class="collapsed">{_("price range")}<span class="selected">{_("Make your choice")}</span></a></h4>')
                    , css_class='widget-boxed-header'),
                Div(
                    Div(
                        Div(
                            Div(
                                Div(
                                    Field('price_range', css_class='radio-custom',
                                          template="crispy/object_list_filter.html",
                                          wrapper_class='no-ul-list filter-list'),
                                    css_class='inner_widget_link'),
                                css_class='card-body pt-0'),
                            css_class='single_filter_card'),
                        css_class='side-list no-border'),
                css_class="widget-boxed-body collapse", css_id='price_range'),
            css_class="single_search_boxed"),
            Div(
                Div(HTML(f'<h4><a href="#amenities" data-toggle="collapse" aria-expanded="false" role="button" class="collapsed">{_("amenities")}<span class="selected">{_("Make your choice")}</span></a></h4>')
                    , css_class='widget-boxed-header'),
                Div(
                    Div(
                        Div(
                            Div(
                                Div(
                                    Field('amenities', css_class='radio-custom',
                                          template="crispy/object_list_filter.html",
                                          wrapper_class='no-ul-list filter-list'),
                                    css_class='inner_widget_link'),
                                css_class='card-body pt-0'),
                            css_class='single_filter_card'),
                        css_class='side-list no-border'),
                css_class="widget-boxed-body collapse", css_id='amenities'),
            css_class="single_search_boxed"),
            Div(
                Submit('submit', _('Show'), css_class='btn btn-md full-width pop-login bg-2'),
                css_class="form-group filter_button")
        )

    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        sqs = self.searchqueryset.all()

        # if self.cleaned_data.get("q"):
        #     sqs = self.searchqueryset.auto_query(self.cleaned_data["q"])
        # else:
        #     sqs = self.searchqueryset.all()

        if self.cleaned_data.get("city"):
            sqs = sqs.filter(city=[self.cleaned_data.get('city')])
        if self.cleaned_data.get('property_types'):
            # details_and_features = models.DetailAndFeature.objects.filter(type=self.cleaned_data.get('property_types')).values_list('rent_object', flat=True)
            details_and_features = models.DetailAndFeature.objects.filter(type=self.cleaned_data.get('property_types')).values_list(flat=True)
            sqs = sqs.filter(details_and_features__in=list(details_and_features))
        if self.cleaned_data.get('bedrooms'):
            bedrooms = [i.property for i in models.DetailAndFeature.objects.filter(
                type=models.DetailAndFeatureType.objects.filter(name='Bedrooms')[0].pk, property=self.cleaned_data.get('bedrooms'))]
            sqs = sqs.filter(bedrooms__in=bedrooms)
        if self.cleaned_data.get('price_range'):
            range = self.cleaned_data.get('price_range').split(',')
            min = int(range[0])
            max = int(range[1])
            rent_objects = [i.price for i in models.RentObject.objects.filter(Q(price__gte=min), Q(price__lte=max))]
            sqs = sqs.filter(price__in=rent_objects)
        if self.cleaned_data.get('amenities'):
            amenities = models.Amenity.objects.filter(pk=self.cleaned_data.get('amenities')).values_list(flat=True)
            sqs = sqs.filter(amenities__in=list(amenities))
        # if self.cleaned_data.get('bedrooms'):
        #     type_bedroom = models.DetailAndFeatureType.objects.filter(name='Bedrooms')[0]
        #     detail_and_feature = models.DetailAndFeature.objects.filter(property=self.cleaned_data.get('bedrooms'), type=type_bedroom.pk)
        #     objects = models.RentObject.objects.filter(id__in=detail_and_feature.values_list('rent_object_id', flat=True))
        #
        #     sqs = sqs.filter(bedrooms=list(objects.values_list('id', flat=True)))


        if self.load_all:
            sqs = sqs.load_all()

        return sqs

    def no_query_found(self):
        return self.searchqueryset.exclude(upc='')


class FilterByNameRentObject(SearchForm):

    def search(self, type):
        if not self.is_valid():
            return self.no_query_found()

        sqs = self.searchqueryset.all()

        if type:
            sqs = sqs.filter(type_of_deal=[type])
        if self.data.get("name"):
            sqs = sqs.filter(name=[self.data.get("name")])

        return sqs