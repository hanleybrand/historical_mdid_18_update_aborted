DEBUG = False
TEMPLATE_DEBUG = DEBUG
LOGGING_OUTPUT_ENABLED = DEBUG



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_test_mdid',
        'USER': 'rooibos',
        'PASSWORD': 'rooibos',
        'HOST': '127.0.0.1',
        'PORT': '',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        },
    }
}
#
# # I checked to make sure that the problems weren't with mysql vs sqlite but sqlite throws amazing errors
# # due to how it handles atomic requests and manual transaction management
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'test.sqllite',
#         'ATOMIC_REQUESTS': True
#     }
# }

CACHE_BACKEND = 'dummy://'

import tempfile

SCRATCH_DIR = tempfile.mkdtemp()
print "Scratch directory for this test session is %s" % SCRATCH_DIR

print "TESTING =========== 1 =================== 2 ================== 3"