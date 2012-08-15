import os.path
import settings
import logging

#csslocal = os.path.join(install_dir, 'rooibos', 'templates_local', 'local.css')
#jslocal = os.path.join(install_dir, 'rooibos', 'templates_local', 'local.css')

#csslocal = os.path.join(install_dir, 'rooibos', 'templates_local', 'local.css')

logging.debug('templates local init' )


if os.path.exists('local.css'):
    settings.LOCAL_CSS += True
if os.path.exists('local.js'):
    settings.LOCAL_JS += True