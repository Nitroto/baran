from .base import *

SITE_HOST = 'http://localhost:8000'
SHOW_API_ROOT = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'baran.sqlite3'),
    }
}

LANGUAGE_CODE = 'en'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
