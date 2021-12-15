from .base import *

MIGRATION_MODULES = DisableMigrations()

PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher', ]

SITE_HOST = 'http://test'

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
