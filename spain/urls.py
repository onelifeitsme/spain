from django.contrib import admin
from django.urls import path, include
from applications.views import IndexView, AboutView, ContactsView
from django.conf.urls.static import static
from django.conf import settings

import debug_toolbar

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
                path('admin/', admin.site.urls),
                path('rosetta/', include('rosetta.urls')),
                path('summernote/', include('django_summernote.urls')),
                path('i18n/', include('django.conf.urls.i18n')),
                # path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
                path('', IndexView.as_view(), name='home'),
                path('', include('applications.objects.urls')),
                path('', include('applications.accounts.urls')),
                path('', include('applications.publications.urls')),
                path('about/', AboutView.as_view(), name='about'),
                path('contacts/', ContactsView.as_view(), name='contacts'),
                path('', include('applications.flatpages_custom.urls')),

)
