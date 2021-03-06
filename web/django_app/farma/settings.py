import os
import markdown
from secret_settings import * 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'markupfield',
    'bootstrap3',
    'selectable',
    'crispy_forms',
    'django_bootstrap_dynamic_formsets',
    'easy_pdf',
    'reportlab',

    'farma',
    'medicamentos',
    'organizaciones',
    'pedidos',
    'usuarios',
    'django_celery_results'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'farma.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'farma.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': os.environ.get('NOMBRE_DB', 'postgres'),
         'USER': os.environ.get('USUARIO_DB', 'postgres'),
         'HOST': os.environ.get('HOST_DB', 'db'),
         'PORT': os.environ.get('PORT_DB', '5432') 
     }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-AR'

TIME_ZONE = 'America/Argentina/Buenos_Aires' 

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# python manage.py collectstatic
STATIC_ROOT = '/var/www/farma.com/static/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "estaticos"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'medios')

MARKUP_FIELD_TYPES = (
    ('markdown', markdown.markdown),
)

LOGIN_URL = '/admin/login'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# VARIABLES PARA CELERY
CELERY_ENABLE_UTC = True  
CELERY_TIMEZONE = "UTC"
CELERY_RESULT_BACKEND = 'django-db'
CELERY_RESULT_BACKEND = 'django-cache'
CELERY_BROKER_URL = 'amqp://guest:guest@rabbit//'

# ENVIO DE MAILS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
