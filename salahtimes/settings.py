import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '^=w(sre0bol)ygy-f64b6c%!^)!6(yxv184s4#gb6#5n*kz57^'


ALLOWED_HOSTS = ["*", ]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'portal',
    # 'accounts',
    'localities',
    'masjids',
    'suggestions',

    'crispy_forms',
    'widget_tweaks',
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

ROOT_URLCONF = 'salahtimes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'salahtimes.wsgi.application'

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


STATIC_URL = '/static/'
SITE_NAME = "Salah Times"
CRISPY_TEMPLATE_PACK = "bootstrap4"


#   PRODUCTION CHANGES


SECURE_SSL_REDIRECT = False
DEBUG = True

import pymysql  # noqa: 402
pymysql.install_as_MySQLdb()

if os.getenv('GAE_APPLICATION', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/salahtimes-265217:asia-south1:salahtimes-v3',
            'USER': 'aamer',
            'PASSWORD': 'Aamer@Salahtimes#',
            'NAME': 'salahtimes_db',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'salahtimes_db',
            'USER': 'aamer',
            'PASSWORD': 'Aamer@Salahtimes#',
        }
    }



if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    SITE_DOMAIN = "http://127.0.0.1:8000"
else:
    SITE_DOMAIN = "https://salahtimes.kondhwa.info"
    STATIC_ROOT = 'static'


EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "mail.salahtimes@gmail.com"
EMAIL_HOST_PASSWORD = "Mail@Salahtimes#*"
EMAIL_USE_TLS = True
ADMIN_EMAILS = ["aameraryan@gmail.com"]
