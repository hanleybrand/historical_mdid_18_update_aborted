import logging
import os, sys
from config.settings import PROJECT_ROOT, ROOIBOS_ROOT,  STATIC_ROOT, MEDIA_ROOT
from config.settings_local import DEBUG, AUTO_STORAGE_DIR, SCRATCH_DIR, LOGGING
import config.settings_local
log = logging.getLogger('rooibos')


log.info('\n\n\n\n====== MDID Startup ===============================================================================')
log.info('Important Directories')
log.info('MDID3 root:     %s', PROJECT_ROOT)
log.info('config dir:     %s', os.path.dirname(config.settings_local.__file__))
log.info('rooibos dir:    %s', ROOIBOS_ROOT)
log.info('media root:     %s', MEDIA_ROOT)
log.info('static files:   %s', STATIC_ROOT)
log.info('scratch dir:    %s', SCRATCH_DIR)
log.info('auto-storage:   %s', AUTO_STORAGE_DIR)
log.info('log file:       %s', LOGGING['handlers']['file']['filename'])
log.info('====end startup messages======================================================\n')
