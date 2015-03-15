import sys
import os
import logging

log = logging.getLogger(__name__)

# Is it useful to put the path to a virtual env?
# VENV_ROOT = os.path.join('/', 'path', 'to','.virtualenvs','hm3')
# or
# V_ROOT = os.path.expanduser('~/.virtualenvs/hm3/')

# the directory containing this directory
PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

# this directory
ROOIBOS_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__)))

# this defines where files will be stored - by default it will be a directory
# that is at the top directory of the mdid3 repo

# DEFAULT_DATA_DIR = os.path.normpath(os.path.join(PROJECT_ROOT, '..' 'mdid-data'))
DEFAULT_DATA_DIR = os.path.normpath(os.path.expanduser('~/dev/mdid-data/hacking-mdid3'))

# Needed to enable compression JS and CSS files
COMPRESS = False
MEDIA_URL = '/static/'
MEDIA_ROOT = os.path.normpath(os.path.join(ROOIBOS_ROOT, 'static'))
SCRATCH_DIR = os.path.normpath(os.path.join(DEFAULT_DATA_DIR, 'mdid-scratch'))
AUTO_STORAGE_DIR = os.path.normpath(os.path.join(DEFAULT_DATA_DIR, 'mdid-collections'))

UPLOAD_LIMIT = 1024 * 1024

# Debug should never be true on a production system
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# set LOGGING_OUTPUT_ENABLED to True to reduce log verbosity
# or False to disable logging
LOGGING_OUTPUT_ENABLED = DEBUG
LOGGING_LOG_SQL = False

# CL_DEBUG when set to true this will output useful info to the terminal or logs
# when mdid3 initializes (see CL_DEBUG section near end of file for what will happen)
CL_DEBUG = True

# TESTING used for running tests to check installation
# set to True before running tests with
# python manage.py test access converters data federatedsearch \
#         artstor presentation statistics storage userprofile util viewers workers
#
# from this directory (PROJECT_ROOT/rooibos/).
# MDID will not function correctly when Testing = True
TESTING = False

ADMINS = (
    #    ('Your name', 'your@email.example'),
)

MANAGERS = ADMINS

# Settings for MySQL
DATABASE_ENGINE = 'mysql'  # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_OPTIONS = {
    'use_unicode': True,
    'charset': 'utf8',
    'init_command': 'SET storage_engine=MyISAM;'
}



# Settings for Microsoft SQL Server (use the appropriate driver setting)
#DATABASE_ENGINE = 'sql_server.pyodbc'
#DATABASE_OPTIONS= {
#    'driver': 'SQL Native Client',             # FOR SQL SERVER 2005
#    'driver': 'SQL Server Native Client 10.0', # FOR SQL SERVER 2008
#    'MARS_Connection': True,
#}

# Settings for all database systems
DATABASE_NAME = 'galleryfork'  # Or path to database file if using sqlite3.
DATABASE_USER = 'fynbos'  # Not used with sqlite3.
DATABASE_PASSWORD = 'fynbos'  # Not used with sqlite3.
DATABASE_HOST = ''  # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''  # Set to empty string for default. Not used with sqlite3.

DEFAULT_CHARSET = 'utf-8'
DATABASE_CHARSET = 'utf8'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'e#!poDuIJ}N,".K=H:T/4z5POb;Gl/N6$6a&,(DRAHUF5c",_p'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

SOLR_URL = 'http://127.0.0.1:8983/solr/'

# Legacy setting for ImageViewer 2 support
SECURE_LOGIN = False

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/'

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

INTERNAL_IPS = ('127.0.0.1',)

HELP_URL = 'http://mdid.org/help/'

DEFAULT_LANGUAGE = 'en-us'

GOOGLE_ANALYTICS_MODEL = True

FLICKR_KEY = 'fbef6e60837b1fb2d354bceee23409be'
FLICKR_SECRET = 'dae5ccee937924f9'

# Set to None if you don't subscribe to ARTstor
ARTSTOR_GATEWAY = None
#ARTSTOR_GATEWAY = 'http://sru.artstor.org/SRU/artstor.htm'

OPEN_OFFICE_PATH = 'C:/Program Files/OpenOffice.org 3/program/'

GEARMAN_SERVERS = ['127.0.0.1']

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'rooibos.auth.ldapauth.LdapAuthenticationBackend',
    #    'rooibos.auth.mailauth.ImapAuthenticationBackend',
    #    'rooibos.auth.mailauth.PopAuthenticationBackend',
)


# List of callables that know how to import templates from various sources.
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.load_template_source',
#    'django.template.loaders.app_directories.load_template_source',
#    #'django.template.loaders.eggs.load_template_source',
#    #'debug_toolbar.templates',
#)

#TEMPLATE_CONTEXT_PROCESSORS = (
#    "django.core.context_processors.auth",
#    "django.core.context_processors.debug",
#    #    "django.core.context_processors.i18n",
#    "django.core.context_processors.media",
#    "django.core.context_processors.request",
#    "rooibos.context_processors.settings",
#    "rooibos.context_processors.selected_records",
#    "rooibos.context_processors.current_presentation",
#)

STORAGE_SYSTEMS = {
    'local': 'rooibos.storage.localfs.LocalFileSystemStorageSystem',
    'online': 'rooibos.storage.online.OnlineStorageSystem',
    'pseudostreaming': 'rooibos.storage.pseudostreaming.PseudoStreamingStorageSystem',
}

LDAP_AUTH = (
    {
        # LDAP Example
        # 'uri': 'ldap://xxxx.xxxxx.edu:xxxx',
        # 'base': 'ou=people,dc=xxxxxxx,dc=edu',
        # 'cn': 'uid',
        # 'dn': 'xxxyour_nic',
        # 'version': 3,
        # 'scope': 1,
        # 'options': {'OPT_X_TLS_TRY': 1,
        #             'OPT_REFERRALS': 0,
        # },
        # 'attributes': ('sn', 'mail', 'givenname', 'eduPersonPrimaryAffiliation'),
        # 'firstname': 'givenname',
        # 'lastname': 'sn',
        # 'email': 'mail',
        #
        # # uncomment this line if your LDAP implementation supports searching without
        # # binding first, and will then allow the user to bind themselves
        # # 'bindname' : 'cn=xxxxxxx,ou=roles,dc=xxxxxx,dc=edu',
        # 'no_bindGetDN': False,
        #
        # # uncomment & change bind_user and bind_password if your LDAP implementation
        # # requires a bind user to authenticate app users
        # 'bind_user': 'cn=xxxxxxxx,ou=roles,dc=xxxxx,dc=edu',
        # 'bind_password': 'xxxxxxxx',
    },
)

SESSION_COOKIE_AGE = 6 * 3600  # in seconds

SSL_PORT = None  # ':443'

# Theme colors for use in CSS
PRIMARY_COLOR = "rgb(152, 189, 198)"
SECONDARY_COLOR = "rgb(118, 147, 154)"

WWW_AUTHENTICATION_REALM = "Please log in to access media from MDID at Your University"

CUSTOM_TRACKER_HTML = ""

EXPOSE_TO_CONTEXT = ('STATIC_DIR', 'PRIMARY_COLOR', 'SECONDARY_COLOR', 'CUSTOM_TRACKER_HTML', 'ADMINS')

# The Megazine viewer is using a third party component that has commercial
# licensing requirements.  To enable the component you need to enter your
# license key, which is available for free for educational institutions.
# See static/megazine/COPYING.
MEGAZINE_PUBLIC_KEY = ""

# To use a commercial licensed flowplayer, enter your flowplayer key here
# and add the flowplayer.commercial-3.x.x.swf file to the
# rooibos/static/flowplayer directory
FLOWPLAYER_KEY = ""

# MDID uses some Yahoo APIs that require an application key
# You can get one at https://developer.apps.yahoo.com/dashboard/createKey.html
YAHOO_APPLICATION_ID = ""

# By default, video delivery links are created as symbolic links. Some streaming
# servers (e.g. Wowza) don't deliver those, so hard links are required.
HARD_VIDEO_DELIVERY_LINKS = False

additional_settings = [
    #    'apps.jmutube.settings_local',
    #    'apps.svohp.settings_local',
    #'apps.mdid-assignments.settings',
    #'apps.webdecks.settings_local',
    #'apps.mdid-sso.settings_sso',
    #'apps.hello-viewer.settings_local_template',
    #'apps.multiviewer.settings_local_template',
]

if DEBUG:
    MIDDLEWARE_CLASSES = (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INSTALLED_APPS = (
        'template_repl',
        'debug_toolbar',
    )

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )

    DEBUG_TOOLBAR_CONFIG = (
        {
            'INTERCEPT_REDIRECTS': False,
            # If set to True (the default) then code in Django itself won't be shown in
            # SQL stacktraces.
            'HIDE_DJANGO_SQL': True,
        }
    )

######--- Wrap up ---######


# This will print a fair amount of information helpful for debugging an installation
# if CL_DEBUG = True at the beginning of this file
# see http://blog.dscpl.com.au/2010/03/improved-wsgi-script-for-use-with.html
#if CL_DEBUG:
#    print "__name__ =", __name__
#    print "__file__ =", __file__
#    print "os.getpid() =", os.getpid()
#    print "os.getcwd() =", os.getcwd()
#    print "os.curdir =", os.path.abspath(os.curdir)
#    #print "sys.path =" # , repr(sys.path)
#    #for forks in sys.path:
#    #    print forks
#    #print "sys.modules.keys() =", repr(sys.modules.keys())
#    print "sys.modules.has_key('rooibos') =", sys.modules.has_key('rooibos')
#    if sys.modules.has_key('rooibos'):
#        print "sys.modules['rooibos'].__name__ =", sys.modules['rooibos'].__name__
#        print "sys.modules['rooibos'].__file__ =", sys.modules['rooibos'].__file__
#        print "os.environ['DJANGO_SETTINGS_MODULE'] =", os.environ.get('DJANGO_SETTINGS_MODULE', None)
#
#    print '===============================\nDirectories\n==============================='
#    print 'project path:  ', PROJECT_ROOT
#    print 'rooibos path:  ', ROOIBOS_ROOT
#    print 'default data:  ', DEFAULT_DATA_DIR
#    print 'scratch:       ', SCRATCH_DIR
#    print 'auto-storage:  ', AUTO_STORAGE_DIR


if CL_DEBUG:
    print "__name__ =", __name__
    print "__file__ =", __file__
    print "os.getpid() =", os.getpid()
    print "os.getcwd() =", os.getcwd()
    print "os.curdir =", os.path.abspath(os.curdir)
    print "sys.path ="  # , repr(sys.path)
    for forks in sys.path:
        print forks
    print "sys.modules.keys() =", repr(sys.modules.keys())
    print "sys.modules.has_key('rooibos') =", sys.modules.has_key('rooibos')
    if sys.modules.has_key('rooibos'):
        print "sys.modules['rooibos'].__name__ =", sys.modules['rooibos'].__name__
        print "sys.modules['rooibos'].__file__ =", sys.modules['rooibos'].__file__
        print "os.environ['DJANGO_SETTINGS_MODULE'] =", os.environ.get('DJANGO_SETTINGS_MODULE', None)

    print '===============================\nDirectories\n==============================='
    print 'project path:  ', PROJECT_ROOT
    print 'rooibos path:  ', ROOIBOS_ROOT
    print 'media root:  ', MEDIA_ROOT
    print 'scratch:       ', SCRATCH_DIR
    print 'auto-storage:  ', AUTO_STORAGE_DIR

######--- Basic Testing or Custom Apps ---######


######--- Logging Setup ---######

#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': True,
#    'formatters': {
#        'standard': {
#            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#            'datefmt': "%d/%b/%Y %H:%M:%S"
#        },
#    },
#    'handlers': {
#        'null': {
#            'level': 'DEBUG',
#            'class': 'django.utils.log.NullHandler',
#        },
#        'logfile': {
#            'level': 'DEBUG',
#            'class': 'logging.handlers.RotatingFileHandler',
#            'filename': DEFAULT_DATA_DIR + "/logs/rooibos.log",
#            'maxBytes': 50000,
#            'backupCount': 2,
#            'formatter': 'standard',
#        },
#        'console': {
#            'level': 'INFO',
#            'class': 'logging.StreamHandler',
#            'formatter': 'standard'
#        },
#    },
#    'loggers': {
#        'django': {
#            'handlers': ['console'],
#            'propagate': True,
#            'level': 'WARN',
#        },
#        'django.db.backends': {
#            'handlers': ['console'],
#            'level': 'DEBUG',
#            'propagate': False,
#        },
#        'rooibos': {
#            'handlers': ['console', 'logfile'],
#            'level': 'DEBUG',
#        },
#    }
#}

