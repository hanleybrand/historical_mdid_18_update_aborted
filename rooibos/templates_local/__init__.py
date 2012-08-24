import os.path
import logging
from django.conf import settings



if os.path.exists('local.css'):
    settings.LOCAL_CSS = True
    logging.debug('LOCAL_CSS: %s' % LOCAL_CSS)
else:
    settings.LOCAL_CSS = False
if os.path.exists('local.js'):
    settings.LOCAL_JS = True
    logging.debug('LOCAL_JS: %s' % LOCAL_JS)
else:
    settings.LOCAL_JS = False
