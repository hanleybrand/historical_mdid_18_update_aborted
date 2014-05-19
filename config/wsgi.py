"""
WSGI config for mdid3 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# TODO: are these sys.path.appends necessary? (they don't seem to be - were in mdid_dj16/dist/linux/django.wsgi file)
#sys.path.append('/var/local/mdid_dj16')
#sys.path.append('/var/local/mdid_dj16/rooibos/contrib')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
