DEBUG = False
TEMPLATE_DEBUG = False
LOGGING_OUTPUT_ENABLED = DEBUG
LOGGING_LOG_SQL = True

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'test.sqlite'

CACHE_BACKEND = 'dummy://'

remove_settings = ['DATABASE_OPTIONS']
remove_settings = ['AUTHENTICATION_BACKENDS']

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    )

import tempfile
SCRATCH_DIR = tempfile.mkdtemp()
print "Scratch directory for this test session is %s" % SCRATCH_DIR
