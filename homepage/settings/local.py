from .base import *

ALLOWED_HOSTS = ["127.0.0.1"]

DEBUG = True

THIRD_PARTY_APPS = ["django_extensions"]

INSTALLED_APPS += THIRD_PARTY_APPS
