"""
Django settings for enstock project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path
import django_heroku
import cloudinary
import cloudinary.uploader
import cloudinary.api


if os.name == 'nt':
    import platform

    OSGEO4W = r"C:\OSGeo4W"
    if '64' in platform.architecture()[0]:
        OSGEO4W += "64"
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-w_wnss3@04%fu58tg81%x7xh*3%445l#-=2i-=ookx-8@*r#+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'core',
    'rest_framework',
    'corsheaders',
    'django_filters',
    'django.contrib.gis',
    'rest_framework_gis',
    'leaflet',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
]

LEAFLET_CONFIG = {
    # you can use your own
    # 'SPATIAL_EXTENT': (5.0, 44.0, 7.5, 46),
    "DEFAULT_CENTER": (-12.0645, -77.0560),
    "DEFAULT_ZOOM": 14,
    "MAX_ZOOM": 20,
    "MIN_ZOOM": 3,
    "SCALE": "both",
    "ATTRIBUTION_PREFIX": "Leaflet map",
    "DEFAULT_PRECISION": 6,
    'RESET_VIEW': False,
}

# JAZZMIN_UI_TWEAKS = {
#     "theme": "minty",
# }

JAZZMIN_SETTINGS = {
    # title of the window
    # "site_title": "Library Admin",
    #
    # # Title on the brand, and the login screen (19 chars max)
    # "site_header": ".",
    #
    # # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    # "site_logo": "logo.png",

    # Relative paths to custom CSS/JS scripts (must be present in static files)
    # "custom_css": "custom.css",
    # "custom_js": None,
    # # Whether to show the UI customizer on the sidebar
    # "show_ui_builder": True,
}

# JAZZMIN_UI_TWEAKS = {
#     "theme": "flatly",
#     "dark_mode_theme": "flatly",
# }

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    'http://localhost:8000',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'enstock.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
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

WSGI_APPLICATION = 'enstock.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'df63cp2ovsdose',
        'USER': 'qjdgmdzahtrtco',
        'PASSWORD': 'aca8af54138d8fa567e5e0bbea07622b9651908af64ac49f1f03b7224b97ffcb',
        'HOST': 'ec2-54-235-116-235.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

# Activate Django-Heroku.
django_heroku.settings(locals())


CLOUDINARY_STORAGE = {
    'CLOUD_NAME':  'enstock',
    'API_KEY':  '781979715613255',
    'API_SECRET':  '2gZE-Ym4syAOI3e7oW4eB7AZfA4'
}