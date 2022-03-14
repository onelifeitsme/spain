# # -*- coding: utf-8 -*-
# import os
# import logging
# from PIL import Image
#
# from django import template
# from django.conf import settings
# from django.contrib.staticfiles import finders
# from django.templatetags.static import static
#
# from django_webp.utils import WEBP_STATIC_URL, WEBP_STATIC_ROOT, WEBP_DEBUG, WEBP_CONVERT_MEDIA_FILES
#
#
# register = template.Library()
#
#
# class WEBPImageConverter:
#
#     def generate_path(self, image_path):
#         """ creates all folders necessary until reach the file's folder """
#         folder_path = os.path.dirname(image_path)
#         if not os.path.isdir(folder_path):
#             os.makedirs(folder_path)
#
#     def get_static_image(self, image_url):
#         return static(image_url)
#
#     def get_generated_image(self, image_url):
#         """ Returns the url to the webp gerenated image,
#         if the image doesn't exist or the generetion fails,
#         it returns the regular static url for the image """
#         real_url = os.path.splitext(image_url)[0] + '.webp'
#         generated_path = os.path.join(WEBP_STATIC_ROOT, real_url)
#         real_url = WEBP_STATIC_URL + real_url
#
#         image_path = finders.find(image_url)
#         if not image_path:
#             return self.get_static_image(image_url)
#
#         if not self.generate_webp_image(generated_path, image_path):
#             return self.get_static_image(image_url)
#         return real_url
#
#     def generate_webp_image(self, generated_path, image_path):
#         if os.path.isfile(generated_path):
#             return True
#
#         try:
#             image = Image.open(image_path)
#         except FileNotFoundError:
#             return False
#
#         try:
#             self.generate_path(generated_path)
#             image.save(generated_path, 'WEBP')
#             return True
#         except KeyError:
#             logger = logging.getLogger(__name__)
#             logger.warn('WEBP is not installed in pillow')
#         except (IOError, OSError):
#             logger = logging.getLogger(__name__)
#             logger.warn('WEBP image could not be saved in %s' % generated_path)
#
#         return False
#
#
# @register.simple_tag(takes_context=True)
# def webp_media(context, value, force_static=WEBP_DEBUG):
#     converter = WEBPImageConverter()
#
#     supports_webp = context.get('supports_webp', False)
#     if not supports_webp or force_static:
#         return converter.get_static_image(value)
#
#     return converter.get_generated_image(value)

from django import template
from django.templatetags.static import static
from django.core.cache import cache

from webp_converter.utils import make_image_key
from webp_converter.models import WebPImage
from django.core.files.storage import default_storage
from PIL import Image
from django.core.files.base import ContentFile
import io

register = template.Library()


def save_webp_image(obj):
    image = Image.open(obj.static_path)
    image_bytes = io.BytesIO()
    image.save(
        fp=image_bytes,
        format="WEBP",
        quality=obj.quality
    )
    image_content_file = ContentFile(content=image_bytes.getvalue())
    default_storage.save(obj.webp_relative_path, image_content_file)


@register.simple_tag(takes_context=True)
def media_webp(context, static_path, quality=80):
    try:
        webp_compatible = context["webp_compatible"]
    except KeyError:
        raise Exception(
            "'webp_converter.context_processors.webp_support' "
            "needs to be added to your context processors."
        )
    if not webp_compatible:
        return static(static_path)
    key = make_image_key(static_path, quality)
    webp_image_url = cache.get(key)
    if not webp_image_url:
        webp_image, _ = WebPImage.objects.get_or_create(
            static_path=static_path, quality=quality
        )
        if not webp_image.webp_image_exists:
            # webp_image.image_absolute_path = 'alksjdf'
            # webp_image.save_webp_image()
           save_webp_image(obj=webp_image)
        webp_image_url = webp_image.webp_url
        cache.set(key, webp_image_url)
    return webp_image_url
