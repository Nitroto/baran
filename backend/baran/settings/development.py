from .base import *

SITE_HOST = 'http://localhost:8000'
SHOW_API_ROOT = True

CSRF_COOKIE_SECURE = False
CORS_ORIGIN_WHITELIST = ['http://localhost:8080', 'http://127.0.0.1:8080']
CSRF_TRUSTED_ORIGINS = ['localhost', '127.0.0.1']

LANGUAGE_CODE = 'en'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
