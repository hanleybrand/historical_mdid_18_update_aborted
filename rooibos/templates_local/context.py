from django.conf import settings
import os.path
import logging

# this was to confirm that a setting from my
# settings_local.py would be available - it was
logging.debug(settings.ADMINS)

try:
    if os.path.exists('templates_local/local.css'):
        settings.LOCAL_CSS = True
    else:
        #local.css is in the same dir as context.py
        settings.LOCAL_CSS = False
        logging.debug('Falserdash! %s is not False at all, I say!' % os.path.exists('local.css'))
    if os.path.exists('templates_local/local.js'):
        settings.LOCAL_JS = True

    else:
        settings.LOCAL_JS = False

    logging.debug('LOCAL_CSS: %s' % settings.LOCAL_CSS)
    logging.debug('LOCAL_JS: %s' % settings.LOCAL_JS)

finally:
    def local_static(context):
        # Make sure to return a dictionary
        logging.debug('returning the locals')
        return {
            'LOCAL_CSS': settings.LOCAL_CSS,
            'LOCAL_JS': settings.LOCAL_JS,
            }


