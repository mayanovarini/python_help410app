"""
WSGI config for help410app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "help410app.settings")

application = get_wsgi_application()

#use whitenoise to serve static files on heroku
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
