"""
Django settings for formal_portfolio project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5wqd09&wvh60g+g881nkr%s7a@sb(78bnh+==dwojf5vozl*&x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio_main',
    'blog',
    'data_viz',
    'storages',
    'boto',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'formal_portfolio.urls'

WSGI_APPLICATION = 'formal_portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__),'static'),)

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "formal_portfolio/static", *MEDIA_URL.strip("/").split("/"))



###################
# S3 STATIC FILES #
###################

AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_ACCESS_KEY_ID ='AKIAJFRYE5UJUMTHGNNA'
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'travisportfolio'
AWS_PRELOAD_METADATA = True #helps collectstatic do updates
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATIC_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/static/'
# STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'
# MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
# MEDIA_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/media/'


try:
    from local_settings import *
except ImportError:
    pass
# Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()
#
# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#
# # Allow all host headers
# ALLOWED_HOSTS = ['*']
#
# # Static asset configuration
# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# # STATIC_ROOT = 'staticfiles'
RESUME_URL = os.path.join(PROJECT_ROOT, "formal_portfolio/static", *MEDIA_URL.strip("/").split("/"))
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

