from .common import *
import os

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
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', '')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'False')
EMAIL_HOST = os.environ.get('EMAIL_HOST','')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'no-reply@example.com')


# CUSTOM PLUGINS

#########################################
## LDAP
#########################################

if os.getenv('TAIGA_ENABLE_LDAP').lower() == 'true':
    # see https://github.com/Monogramm/taiga-contrib-ldap-auth-ext
    print("Taiga contrib LDAP Auth Ext enabled")
    INSTALLED_APPS += ["taiga_contrib_ldap_auth_ext"]
    LDAP_SERVER = os.environ.get('LDAP_SERVER', 'ldap://example.com')
    LDAP_PORT = os.environ.get('LDAP_PORT', 636)
    LDAP_START_TLS = os.environ.get('LDAP_START_TLS', False)
    LDAP_BIND_DN = os.environ.get('LDAP_BIND_DN', 'CN=SVC Account,OU=Service Accounts,OU=Servers,DC=example,DC=com')
    LDAP_BIND_PASSWORD = os.environ.get('LDAP_BIND_PASSWORD', '<REPLACE_ME>')
    LDAP_SEARCH_BASE = os.environ.get('LDAP_SEARCH_BASE', 'OU=DevTeam,DC=example,DC=net')
    LDAP_USERNAME_ATTRIBUTE = os.environ.get('LDAP_USERNAME_ATTRIBUTE', 'uid')
    LDAP_EMAIL_ATTRIBUTE = os.environ.get('LDAP_EMAIL_ATTRIBUTE', 'mail')
    LDAP_FULL_NAME_ATTRIBUTE = os.environ.get('LDAP_FULL_NAME_ATTRIBUTE', 'displayName')


#########################################
## GITLAB
#########################################

if os.getenv('TAIGA_ENABLE_GITLAB_AUTH').lower() == 'true':
    # see https://github.com/taigaio/taiga-contrib-gitlab-auth
    print("Taiga contrib GitLab Auth enabled")
    INSTALLED_APPS += ["taiga_contrib_gitlab_auth"]

    # Get these from Admin -> Applications
    GITLAB_URL = os.getenv('TAIGA_GITLAB_AUTH_URL')
    GITLAB_API_CLIENT_ID = os.getenv('TAIGA_GITLAB_AUTH_CLIENT_ID')
    GITLAB_API_CLIENT_SECRET = os.getenv('TAIGA_GITLAB_AUTH_CLIENT_SECRET')