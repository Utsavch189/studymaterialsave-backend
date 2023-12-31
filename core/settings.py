"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import datetime,os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fp)205*2hf@tdd3d*j^@46%c-qd21b1^k!=m3=e#6ph=exy8wh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'django_crontab',
    'cloudinary_storage',
    'cloudinary',
    'dbbackup',
    'rest_framework',
    'corsheaders',
    'apps.auths.apps.AuthConfig',
    'apps.posts.apps.PostsConfig',
    'apps.sections.apps.SectionsConfig',
    'apps.sharing.apps.SharingConfig',
    'apps.users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.authorization.main.Authorization'
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dcf6uk047',
    'API_KEY': '176572318442856',
    'API_SECRET': 'C0hg2pOkd-7MoOdoeXLcF-RMHTk'
}


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ],
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

#SMTP setup
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST="smtp.gmail.com"
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER="utsavpokemon9000chatterjee@gmail.com"
EMAIL_HOST_PASSWORD="mrrydilzvjzazkud"

CORS_ALLOW_CREDENTIALS = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING ={
    'version':1,
    "disable_existing_loggers": False,
    'loggers':{
        'mylogger':{
            'handlers':['file'],
            'level':'INFO',
        }
    },
    'handlers':{
        'file':{
            'class': 'logging.FileHandler',
            'filename':'logs/'+str(datetime.date.today())+'.log',
            'formatter':'myforamt'
        }
    },
    'formatters':{
        'myforamt': {
            'format': '{levelname} : [{asctime} {module} {lineno:d} {process:d} {thread:d} {message}]',
            'datefmt' : "%d/%b/%Y %H:%M:%S",
            'style': '{',
        }

    }
}

APPEND_SLASH=False

CORS_ORIGIN_ALLOW_ALL=False
CORS_ORIGIN_WHITELIST = (
  'http://localhost:3000',
 'http://localhost:3001' 
  )
CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "x-userid"
)
CSRF_TRUSTED_ORIGINS=['http://localhost:3000','http://localhost:3001'
]
