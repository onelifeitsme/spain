from django.conf import settings
from django_google_maps.widgets import GoogleMapsAddressWidget

class GoogleMapsAddressWidgetExt(GoogleMapsAddressWidget):

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js',
            'https://maps.google.com/maps/api/js?key={}&libraries=places'.format(
                settings.GOOGLE_MAPS_API_KEY),
            'assets/js/django_google_maps_ext.js',
        )