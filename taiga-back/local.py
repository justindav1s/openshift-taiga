from .common import *
import os

try:
    from .logging import *
except ImportError:
    pass

LOGLEVEL = os.environ.get('LOGLEVEL', 'debug').upper()
DEBUG = os.environ.get('DEBUG', 'False')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':  os.environ.get('DATABASE_NAME', 'taiga'),
        'USER':  os.environ.get('DATABASE_USER', 'taiga'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_SERVICE_NAME', 'postgresql'),
        'PORT': '5432',
    }
}

SITES["front"]["scheme"] = os.environ.get('TAIGA_FRONT_SCHEME', 'https')
SITES["front"]["domain"] = os.environ.get('TAIGA_FRONT_DOMAIN', 'test.com')

SITES["api"]["scheme"] = os.environ.get('TAIGA_BACK_SCHEME', 'https')
SITES["api"]["domain"] = os.environ.get('TAIGA_BACK_DOMAIN', 'other.com')


MEDIA_URL = os.environ.get('TAIGA_MEDIA_URL', SITES["api"]["scheme"] + '://' + SITES["api"]["domain"] + '/media/')
STATIC_URL = os.environ.get('TAIGA_STATIC_URL', SITES["api"]["scheme"] + '://' + SITES["api"]["domain"] + '/static/')

MEDIA_ROOT = os.environ.get('HOME')+'/media'
STATIC_ROOT = os.environ.get('HOME')+'/static'

# disable public registration by default
PUBLIC_REGISTER_ENABLED = os.environ.get('PUBLIC_REGISTER_ENABLED', False)

DEFAULT_FROM_EMAIL = os.environ.get('TAIGA_FROM_EMAIL_ADDRESS', 'no-reply@example.com')
# SERVER_EMAIL = DEFAULT_FROM_EMAIL

#CELERY_ENABLED = True

# EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
# EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://taiga:PASSWORD_FOR_EVENTS@localhost:5672/taiga"}

# Uncomment and populate with proper connection parameters
# for enable email sending. EMAIL_HOST_USER should end by @domain.tld
# EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', '')
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'False')
# EMAIL_HOST = os.environ.get('EMAIL_HOST','')
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
# EMAIL_PORT = os.environ.get('EMAIL_PORT', '')
# DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'no-reply@example.com')