from admin_exam.send_email import *
from admin_exam.mysql import *

"""
Django settings for ExamSoftware project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^s#js!rnkll3g3h248sm_-j-+gbawi1dv+x2v$siu1z$=p#q*4'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
# DEBUG = False

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # 'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'django_mathjax',
    'admin_exam',
    'student',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ExamSoftware.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ExamSoftware.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': ENGINE,
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'Asia/Ho_Chi_Minh'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

EMAIL_HOST = EMAIL_HOST
EMAIL_PORT = EMAIL_PORT
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_USE_SSL = EMAIL_USE_SSL


MEDIA_URL = '/media/assets/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/assets')

MATHJAX_ENABLED = True
MATHJAX_LOCAL_PATH = 'student/js/mathjax/'
MATHJAX_CONFIG_FILE = "TeX-MML-AM_CHTML"
MATHJAX_CONFIG_DATA = {
    "tex2jax": {
        "inlineMath":
        [
            ['$', '$'],
            ['\\(', '\\)']
        ]
    }
}


# SUIT_CONFIG = {
#     # header
#     'ADMIN_NAME': 'Administration',
#     'HEADER_DATE_FORMAT': 'l, j. F Y',
#     'HEADER_TIME_FORMAT': 'H:i',

#     # forms
#     'SHOW_REQUIRED_ASTERISK': True,  # Default True
#     'CONFIRM_UNSAVED_CHANGES': True,  # Default True

#     # menu
#     'SEARCH_URL': '/admin/auth/user/',
#     'MENU_ICONS': {
#         'sites': 'icon-leaf',
#         'auth': 'icon-lock',
#     },
#     'MENU_OPEN_FIRST_CHILD': True,  # Default True
#     'MENU_EXCLUDE': ('auth.group',),
#     'MENU': (
#         'sites',
#         {'app': 'auth', 'icon': 'icon-lock', 'models': ('user', 'group')},
#         {'label': 'Settings', 'icon': 'icon-cog',
#             'models': ('auth.user', 'auth.group')},
#         {'label': 'Support', 'icon': 'icon-question-sign', 'url': '/support/'},
#     ),

#     # misc
#     'LIST_PER_PAGE': 15
# }
