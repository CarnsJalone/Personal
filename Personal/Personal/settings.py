"""
Django settings for Personal project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys
import json
import logging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGGING_DIR = os.path.join(BASE_DIR, 'Home/Logging')

sys.path.append(LOGGING_DIR)

logging.basicConfig(filename=os.path.join(LOGGING_DIR, 'logger.txt'), level=logging.DEBUG)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# Function to read in credentials, this determines if we are on our local server
# Or deployed
if os.path.isfile('/home/jarret/Documents/Python/Credentials/Personal/credentials.json'):
    with open('/home/jarret/Documents/Python/Credentials/Personal/credentials.json') as credentials:
        data = json.loads(credentials.read())
elif os.path.isfile('/opt/Credentials/Personal/credentials.json'):
    with open('/opt/Credentials/Personal/credentials.json') as credentials:
        data = json.loads(credentials.read())
else:
    logging.critical("Unable to read in necessary credentials, unable to proceed...")


# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = data["Personal_Credentials"][0]["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['206.81.4.37', '127.0.0.1', 'localhost', 'carnsjalone.com', 'www.carnsjalone.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'Home.apps.HomeConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Personal.urls'

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

WSGI_APPLICATION = 'Personal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # os.path.join(BASE_DIR, 'Home/Logging')
]

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

HOME_DIRECTORY = os.path.join(BASE_DIR, 'Home')

PDF_PARSER_DIRECTORY = os.path.join(HOME_DIRECTORY, 'PDF_Parser')

MEDIA_ROOT = os.path.join(PDF_PARSER_DIRECTORY, 'Uploaded_Files')

MEDIA_URL = '/media/'

# Email Preferences

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = data["Personal_Credentials"][0]["Personal_Email_Username"]
EMAIL_HOST_PASSWORD = data["Personal_Credentials"][0]["Personal_Email_Password"]
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# Error Reporting
SERVER_EMAIl = data["Personal_Credentials"][0]["Personal_Email_Username"]
