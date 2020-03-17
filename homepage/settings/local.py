from .base import *

ALLOWED_HOSTS = ["127.0.0.1"]

DEBUG = True

THIRD_PARTY_APPS = ["django_extensions"]

INSTALLED_APPS += THIRD_PARTY_APPS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "ATOMIC_REQUESTS": True,
        "AUTOCOMMIT": True,
        "NAME": "homepage",
    }
}
