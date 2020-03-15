"""
WSGI config for homepage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

from apig_wsgi import make_lambda_handler
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homepage.settings')

application = get_wsgi_application()

lambda_handler = make_lambda_handler(application)
