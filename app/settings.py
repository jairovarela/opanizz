""" 
Django settings for app project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1*%ml73+*b79x%&5blr5x&jsz92qj9y^$1eq(&x@&9un+k*h2^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#DESARROLLO

ALLOWED_HOSTS = ['administracion.opaniz.com','82.223.14.157','127.0.0.1']

#PRODUCCION

#ALLOWED_HOSTS = ['administracion.opaniz.com']

# Application definition

INSTALLED_APPS = [

    'administracion',
    'clientes',
    'contratos',
    'generalidades',
    'factura',
    'wkhtmltopdf',
    'django_select2',
    'django_extensions',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
    'registration',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

SITE_ID = 5

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        #'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'admin_tools.template_loaders.Loader',
            ]
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-la'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static_pro", "static")]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_env", "static_root")
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_env", "media_root")

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

CACHE_BACKEND = 'select2'

ADMIN_TOOLS_MENU = 'menu.CustomMenu'
ADMIN_TOOLS_THEMING_CSS = 'admin_tools/css/theming.css'


#CONFIGURACION DE REGISTRATION-REDUX
#ACTIVATION_EMAIL_SUBJECT = [os.path.join(BASE_DIR, '/templates/registration/activation_email_subject.txt')]
#ACTIVATION_EMAIL_BODY = [os.path.join(BASE_DIR, '/templates/registration/activation_email.txt')]
#ACTIVATION_EMAIL_HTML = [os.path.join(BASE_DIR, '/templates/registration/activation_complete.html')]
REGISTRATION_OPEN = True                # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = False  # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/accounts/dashboard/'  # The page you want users to arrive at after they successful log in
LOGIN_URL = '/accounts/login/'  # The page users are directed to if they are not logged in,
#  and are trying to access pages requiring authentication



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.1and1.es'
EMAIL_HOST_USER = 'no-reply@administracion.opaniz.com'
EMAIL_HOST_PASSWORD = '1q2w3e4r'
EMAIL_PORT = 587
#DEFAULT_FROM_EMAIL = 'webmaster@localhost'


GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}
