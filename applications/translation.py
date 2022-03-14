from modeltranslation.translator import register, TranslationOptions

from applications.models import AboutUsText, AboutUsDetailInformation
from applications.publications.models import Blog
from applications.seo.models import MainSeo

#
# @register(AboutUsText)
# class AboutUsTextTranslationOptions(TranslationOptions):
#     fields = ('text_0',)
#
#
# @register(AboutUsDetailInformation)
# class AboutUsDetailInformationTranslationOptions(TranslationOptions):
#     fields = ('title_1', 'subtitle_1', 'title_2', 'subtitle_2', 'title_3', 'subtitle_3', 'title_4', 'subtitle_4',)
#
#
# @register(Blog)
# class BlogUsTranslationOptions(TranslationOptions):
#     fields = ('title', 'short_description', 'description', 'seo_keywords', 'seo_description', 'seo_title',)
#
#
# @register(MainSeo)
# class MainSeoTranslationOptions(TranslationOptions):
#     fields = ('seo_text', 'seo_keywords', 'seo_description', 'seo_title',)
