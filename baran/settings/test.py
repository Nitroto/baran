from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'test.sqlite3'),
        'TEST': {
            # Don't test migrations New in Django 3.1.
            'MIGRATE': False,
        },
    }
}

PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher', ]

SITE_HOST = 'http://test'
