import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_ID = 1

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wg6rsgwi*(ptb)6y@^hpjjm1f63&$=q24h5%6-84vn!ohrnm+r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# DEFAULT_HOST = '127.0.0.1'
ALLOWED_HOSTS = ['127.0.0.1', 'spain.nextner.com', 'h2srealestate.com']

AUTH_USER_MODEL = 'accounts.User'

EMAIL_PORT = 1025
SERVER_EMAIL = 'django@nextner.ru'
EMAIL_HOST = '127.0.0.1'

# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = '/tmp/app-messages' # change this to a proper location

GOOGLE_MAPS_API_KEY = "AIzaSyCMfWNDie3NnXO3c8MZ0h9HNPChnmb5qwU"
# Application definition


# INTERNAL_IPS = ("127.0.0.1",)

INSTALLED_APPS = [
    # 'modeltranslation',
    'applications',
    'applications.publications',
    'applications.accounts',
    'applications.objects',
    'applications.currencies',
    'applications.seo',
    'applications.search',
    'applications.flatpages_custom',
    'django_filters',

    'bootstrap4',
    'easy_thumbnails',
    'django_summernote',
    'phonenumbers',
    'haystack',
    'django_google_maps',
    'django.contrib.flatpages',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'webp_converter',
    # 'debug_toolbar',
    'adminsortable2',
    'rosetta',
    'parler',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',

]


ROOT_URLCONF = 'spain.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join('templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'builtins': [
                # 'django_hosts.templatetags.hosts_override',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'spain.context_processors.about_us_context_processor',
                'spain.context_processors.modal_login_context_processor',
                'spain.context_processors.modal_signup_context_processor',
                # 'applications.search.context_processors.search_form',

                'django.template.context_processors.i18n',
                'webp_converter.context_processors.webp_support',
                'applications.seo.context_processors.seo_by_path',

            ],
        },
    },
]

WSGI_APPLICATION = 'spain.wsgi.application'

LOGIN_REDIRECT_URL  =  '/'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + '/' + 'db.sqlite3',

    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}
HAYSTACK_DOCUMENT_FIELD = 'content'
HAYSTACK_ITERATOR_LOAD_PER_QUERY = 1000

# When adding, modifying and deleting data, automatically generate index


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


gettext = lambda s: s

LANGUAGES = (
    ('en', gettext('English')),
    ('ru', gettext('Russian')),

)

PARLER_DEFAULT_LANGUAGE_CODE = 'en'
PARLER_LANGUAGES = {
    SITE_ID: (
        {'code': 'en',},
        {'code': 'ru',},
    ),
    'default': {
        'fallback': 'en',             # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,   # the default; let .active_translations() return fallbacks too.
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_components'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SUMMERNOTE_THEME = 'bs4'
