import logging
import os
from django.conf import settings
try:
    import config.settings_local as settings_file
except ImportError:
    import config.settings as settings_file

log = logging.getLogger(__name__)

log.info('\n\n\n\n====== MDID Startup ===============================================================================')
log.info('Important Directories')
log.info('MDID3 root:     %s', settings.PROJECT_ROOT)
log.info('config dir:     %s', os.path.dirname(settings_file.__file__))
log.info('rooibos dir:    %s', settings.ROOIBOS_ROOT)
log.info('media root:     %s', settings.MEDIA_ROOT)
log.info('static files:   %s', settings.STATIC_ROOT)
log.info('scratch dir:    %s', settings.SCRATCH_DIR)
log.info('auto-storage:   %s', settings.AUTO_STORAGE_DIR)
log.info('log file:       %s', settings.LOGGING['handlers']['rooibos']['filename'])
log.info('====end startup messages======================================================\n')
