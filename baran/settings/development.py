from .base import *

SITE_HOST = 'http://localhost:8000'
SHOW_API_ROOT = True

CORS_ORIGIN_WHITELIST = ['http://localhost:8080', 'http://127.0.0.1:8080', 'http://0.0.0.0:8000']
CSRF_TRUSTED_ORIGINS = ['localhost', '127.0.0.1', '0.0.0.0']

LANGUAGE_CODE = 'en'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
