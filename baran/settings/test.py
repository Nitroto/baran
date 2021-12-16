from .base import *

MIGRATION_MODULES = DisableMigrations()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'baran.sqlite3'),
    }
}

PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher', ]

SITE_HOST = 'http://test'

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
