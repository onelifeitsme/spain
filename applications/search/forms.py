from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit
from django import forms
from haystack.forms import SearchForm


from applications.objects.models import RentObject, Category


def get_countries():
    countries = []
    for obj in RentObject.objects.all():
        if obj.country not in [item[1] for item in countries]:
            countries.append((obj.id, obj.country))
    return [('', '')] + countries


def get_cities():
    cities = []
    for obj in RentObject.objects.all():
        if obj.city not in [item[1] for item in cities]:
            cities.append((obj.id, obj.city))
    return [('', '')] + cities


class CitySelect(forms.Select):
    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs)
        try:
            self.countries_cities = {obj.id: obj.country for obj in RentObject.objects.all()}
        except Exception as e:
            pass
        finally:
            self.choices = list(choices)

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        options = super(CitySelect, self).create_option(name, value, label, selected, index, subindex=None, attrs=None)
        if options['label'] != '':
            options['attrs']['data_country'] = self.countries_cities.get(options['value'])
            options['value'] = options['value']
        else:
            options['attrs']['data_country'] = ''
        return options


class BaseSearchForm(SearchForm):
    category = forms.ModelChoiceField(
        required=False,
        label=_('Type'),
        queryset=Category.objects.all(),
        empty_label=_('All'))
    type_of_deal = forms.ChoiceField(
        required=False,
        label=_('For'),
        choices=[('', _('All'))] + RentObject.TYPE_OF_DEAL_CHOICES,
        widget=forms.Select())
    price_to = forms.IntegerField(required=False, label=_('Price to'))
    country = forms.ChoiceField(required=True,
                                choices=get_countries,
                                label=_('Country'),
                                widget=forms.Select())
    city = forms.ChoiceField(required=True,
                             choices=get_cities,
                             label=_('City'),
                             widget=CitySelect())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'search_form'
        # self.helper.form_class = 'row'
        self.helper.form_method = 'get'
        self.helper.form_action = 'search_result'
        self.helper.form_show_labels = True
        self.helper.disable_csrf = False
        self.helper.use_custom_control = True
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        Div(
                            Field('category', css_class='form-control', placeholder=_("Type")),
                            css_class='input-with-icon'),
                        css_class='form-group'),
                    css_class='col-lg-2 col-md-2 col-sm-12'),
                Div(
                    Div(
                        Div(
                            Field('type_of_deal', css_class='form-control', placeholder="Looking"),
                            css_class='input-with-icon'),
                        css_class='form-group'),
                    css_class='col-lg-2 col-md-2 col-sm-12'),
                Div(
                    Div(
                        Div(
                            Field('price_to', css_class='form-control', placeholder=_("Price to")),
                            css_class='input-with-icon'),
                        css_class='form-group'),
                    css_class='col-lg-2 col-md-2 col-sm-12'),
                Div(
                    Div(
                        Div(
                            Field('country', css_class='form-control', placeholder="Country"),
                            css_class='input-with-icon'),
                        css_class='form-group none'),
                    css_class='col-lg-2 col-md-2 col-sm-12'),
                Div(
                    Div(
                        Div(
                            Field('city', css_class='form-control', placeholder=_("City")),
                            css_class='input-with-icon'),
                        css_class='form-group none'),
                    css_class='col-lg-2 col-md-2 col-sm-12'),
                Div(
                    Div(
                        Submit('submit', _('Search'), css_class='btn search-btn'),
                        css_class='form-group none'),
                    css_class='col-lg-2 col-md-2 col-sm-12 small-padd'),
                css_class="row"),
        )

    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        sqs = self.searchqueryset.all()
        # if self.cleaned_data.get("q"):
        #     sqs = self.searchqueryset.auto_query(self.cleaned_data["q"])
        # else:
        #     sqs = self.searchqueryset.all()

        if self.cleaned_data.get("category"):
            sqs = sqs.filter(category=[self.cleaned_data.get('category')])
        if self.cleaned_data.get("type_of_deal"):
            sqs = sqs.filter(type_of_deal=[self.cleaned_data.get('type_of_deal')])
        if self.cleaned_data.get("price_from") and self.cleaned_data.get("price_to"):
            sqs = sqs.filter(price__range=[self.cleaned_data.get('price_from'),
                                           self.cleaned_data.get('price_to')])
        if self.cleaned_data.get("country"):
            rent_object = RentObject.objects.get(id=self.cleaned_data.get('country'))
            country = rent_object.country
            sqs = sqs.filter(country=country)
        if self.cleaned_data.get("city"):
            rent_object = RentObject.objects.get(id=self.cleaned_data.get('city'))
            city = rent_object.city
            sqs = sqs.filter(city=city)

        if self.load_all:
            sqs = sqs.load_all()

        return sqs

    def no_query_found(self):
        return self.searchqueryset.exclude(upc='')
