from .models import MainSeo
from django.conf import settings

def seo_by_path(request):
    if settings.USE_I18N:
        path = request.path_info.replace('/' + request.LANGUAGE_CODE, '')
        seo = MainSeo.get_nearest(path)
    else:
        seo = MainSeo.get_nearest(request.path_info)
    return {'seo': MainSeo.as_dict(seo) if seo else {}}
