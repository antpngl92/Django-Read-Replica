import os

from .env import env, environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
ROOT_DIR = environ.Path(__file__) - 2

env.read_env(os.path.join(ROOT_DIR, ".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@rz0633vd$6e+=m@ha1-t&e(ua$r6##4k4(h%d$5v+3ar@7n^9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'newsletter',
    'debug_toolbar',

]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'read_replica.urls'

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

WSGI_APPLICATION = 'read_replica.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

USE_READ_REPLICA = env.bool('USE_READ_REPLICA', default=False)
READ_REPLICA_DATABASE_NAME = env.str('READ_REPLICA_DATABASE_NAME', default='read_replica')

DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres:///main'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

if USE_READ_REPLICA:
    DATABASES[READ_REPLICA_DATABASE_NAME] = env.db(
        'READ_REPLICA_DATABASE_URL',
        'postgres:///replica'
    )

    # We don't want atomic requests for the read replica since we are not going to write to it
    DATABASES[READ_REPLICA_DATABASE_NAME]['ATOMIC_REQUESTS'] = False

    # Only if the read replica is in play, we need additional database router
    DATABASE_ROUTERS = ['utils.database_routers.DjangoModelsRouter']


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATIC_ROOT = str(ROOT_DIR('staticfiles'))


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.abspath(os.path.join(ROOT_DIR, '..', 'media'))
