"""
Production Settings for Heroku
"""
import dj_database_url

from .base import *

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=env.bool('SSL_REQUIRE', default=False))
}

CORS_ORIGIN_WHITELIST = []
CSRF_TRUSTED_ORIGINS = ['simpleemployee.herokuapp.com']
