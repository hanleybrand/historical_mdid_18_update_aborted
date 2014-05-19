import sys
import os
import logging
log = logging.getLogger(__name__)

###-### directory variables  #####-##### #####-##### #####-##### #####-##### #####-##### #####-##### #####-##### #####
# self set directory paths based on local file locations
# note: mdid_dj16 data is stored outside of the config file hierarchy, i.e.
# /var/local/
# |-- mdid_dj16
# |   |-- config/
# |   |-- rooibos/
# |   |-- manage.py
# |-- mdid_dj16-data
# |   |-- rooibos/
# |   |-- rooibos/
# ... etc.

# MDID repo root
PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '../'))
# the rooibos directory
ROOIBOS_ROOT = os.path.normpath(os.path.join(PROJECT_ROOT, 'rooibos'))

# STATIC_FILES
# where non-dynamic files are stored (i.e. javascript libraries, css, etc.)
STATIC_ROOT = os.path.normpath(os.path.join(PROJECT_ROOT, 'static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.normpath(os.path.join(ROOIBOS_ROOT, 'static')),
)


#####-##### Local Data #####-##### #####-##### #####-##### #####-##### #####-##### #####-##### #####-##### #####-#####

# this defines where files will be stored - by default it will be a directory
# called mdid_dj16-data that is in the same directory as PROJECT_ROOT (stored outside of the application)
#DEFAULT_DATA_DIR = os.path.normpath(os.path.join(PROJECT_ROOT, '../', 'mdid_dj16-data/'))
DEFAULT_DATA_DIR = os.path.normpath(os.path.join(PROJECT_ROOT, '../', 'mdid-data/', 'mdid3-data'))
DEFAULT_CUSTOM_DIR = os.path.normpath(os.path.join(PROJECT_ROOT, '../', 'mdid-data/', 'local_static'))

# scratch_dir is where non-permanent files (including image thumbnails) are stored
SCRATCH_DIR = os.path.normpath(os.path.join(DEFAULT_DATA_DIR, 'mdid-scratch'))
# storage for files not defined by storage?
# TODO: get better definition for what AUTO_STORAGE_DIR is for
AUTO_STORAGE_DIR = os.path.normpath(os.path.join(DEFAULT_DATA_DIR, 'mdid_dj16-collections'))

###-### MEDIA settings
#  (i.e. media associated with records)
MEDIA_URL = '/media/'
MEDIA_ROOT = DEFAULT_DATA_DIR
UPLOAD_LIMIT = 1024 * 1024

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# enable compression (i.e. minification) JS and CSS files - set to True or False
COMPRESS = False

# Where django templates are loaded from - in general, adding to this is ok - don't remove directories
# TODO: look into if it's possible to allow overloading django templates via ordering of directories below
# TODO: Move unchangeable dirs to settings.py
TEMPLATE_DIRS = (
    os.path.normpath(os.path.join(ROOIBOS_ROOT, 'templates')),
    os.path.normpath(os.path.join(ROOIBOS_ROOT, 'access', 'templates')),
    os.path.normpath(os.path.join(ROOIBOS_ROOT, 'ui', 'templates')),
    os.path.normpath(os.path.join(ROOIBOS_ROOT, 'contrib', 'google_analytics', 'templates')),
    # empty by default
    os.path.normpath(os.path.join(PROJECT_ROOT, 'templates')),
)

MASTER_TEMPLATE = 'master_root.html'

####-DEBUG/SETUP Variables-####
# All variables in this section should be False on a production system
#
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Temp variable to selectively disable problematic modules - setting to true will cause errors.
# see below todos for specific modules
# TODO: /rooibos/util/stats_middleware.py - throws errors with django 1.6
NOT_WORKING = False

# CL_DEBUG when set to true this will output arguably useful info to the terminal or logs
# when config initializes, including python paths, etc.
# possible values are: True, False or Full
# (see CL_DEBUG section near end of file for what will happen)
CL_DEBUG = True

# TESTING used for running tests to check installation
# set to True before running tests with
#     python manage.py test access converters data federatedsearch \
#         artstor presentation statistics storage userprofile util viewers workers
#
# from this directory (PROJECT_ROOT/rooibos/).
# MDID will not function correctly when Testing = True
TESTING = False


#####-##### Local MDID Settings #####-##### #####-##### #####-##### #####-##### #####-##### #####-##### #####-#####

# Settings in this section allow customization of your MDID installation
# You can put local files in mdid_dj16-data/local_static and
# add reference them like:
# LOGO_URL = os.path.normpath(os.path.join(DEFAULT_CUSTOM_DIR, 'logo.png'))
# FAVICON_URL = os.path.normpath(os.path.join(DEFAULT_CUSTOM_DIR, 'favico.ico'))

LOGO_URL = None
FAVICON_URL = os.path.normpath(os.path.join(STATIC_URL, 'images', 'favicon.ico'))
COPYRIGHT = None
TITLE = None

WWW_AUTHENTICATION_REALM = "Please log in to access media from MDID at Your University"
SHOW_FRONTPAGE_LOGIN = 'yes'

ADMINS = (
#    ('Your name', 'your@email.example'),
)
MANAGERS = ADMINS
# accessing mdid_dj16 from any ip listed below will change the following behaviors:
# see debug comments, when DEBUG is True
# debug_toolbar (if installed) will act as if debug=true
INTERNAL_IPS = ('127.0.0.1',)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
# TODO: Check how the revised UTC handling in django 1.6 affects the TIME_ZONE setting
TIME_ZONE = 'America/New_York'

# Make this unique, and don't share it with anybody.
# you can generate a key in a terminal by issuing the below command in PROJECT_ROOT
# python manage.py generate_secret_key
# --> !0hbkf##*39#vgkra-d$2_x8^#4^2qmw1pa*@x4%otfvczt#*j
SECRET_KEY = 'Make this unique, and don\'t share it with anybody.'

SESSION_COOKIE_AGE = 6 * 3600  # in seconds

# Requires valid ssl cert, otherwise set to None
SSL_PORT = None  # ':443'
# Legacy setting for ImageViewer 2 support
SECURE_LOGIN = False


# Theme colors for use in CSS
PRIMARY_COLOR = "rgb(152, 189, 198)"
SECONDARY_COLOR = "rgb(118, 147, 154)"

EXPOSE_TO_CONTEXT = ('STATIC_DIR', 'PRIMARY_COLOR', 'SECONDARY_COLOR', 'CUSTOM_TRACKER_HTML', 'ADMINS')

HELP_URL = 'http://mdid_dj16.org/help/'

DEFAULT_LANGUAGE = 'en-us'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/'

#####-##### Database settings #####-##### #####-##### #####-##### #####-##### #####-##### #####-##### #####-#####

## Settings for MySQL are included
## see https://docs.djangoproject.com/en/1.6/ref/databases/#oracle-notes for Oracle Setup

#  settings below  will work if you exec MYSQL_INIT in

    # CREATE DATABASE rooibos CHARACTER SET utf8;
    # GRANT ALL PRIVILEGES ON rooibos.* TO rooibos@localhost
    # IDENTIFIED BY 'rooibos';
    # UPDATE mysql.user SET Select_priv='Y',Insert_priv='Y', Update_priv='Y',Delete_priv='Y',
    # Create_priv='Y', Drop_priv='Y',Index_priv='Y',Alter_priv='Y'
    # WHERE Host='localhost' AND User='rooibos';
    # FLUSH PRIVILEGES;

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rooibos',
        'USER': 'rooibos',
        'PASSWORD': 'rooibos',
        # empty string with host & port = default
        # start host with a forward slash with MySQL to connect via a Unix socket, i.e.
        # "HOST": '/var/run/mysql',
        'HOST': '127.0.0.1',
        'PORT': '',
        # TODO: test CONN_MAX_AGE (throws error if set to None)
        #  lifetime of a database connection, in seconds - 0 is the old behavior, None = unlimited persistent connections
        # 'CONN_MAX_AGE': 'None',
        'OPTIONS': {
            # change init_command if you want to specify what mysql engine to use
            # 'init_command': 'SET storage_engine=INNODB',
        },
    }
}

DEFAULT_CHARSET = 'utf-8'
DATABASE_CHARSET = 'utf8'
#
# TODO: Does MS SQL Server still work with django 1.6? - any changes necessary?
# see also http://django-mssql.readthedocs.org/en/latest/
# Settings for Microsoft SQL Server (use the appropriate driver setting)
#DATABASE_ENGINE = 'sql_server.pyodbc'
#DATABASE_OPTIONS= {
#    'driver': 'SQL Native Client',             # FOR SQL SERVER 2005
#    'driver': 'SQL Server Native Client 10.0', # FOR SQL SERVER 2008
#    'MARS_Connection': True,
#}
####
#

#####-##### External app & service settings #####-##### #####-##### #####-##### #####-##### #####-##### #####-#####
#
# External Dependencies
#
SOLR_URL = 'http://127.0.0.1:8983/solr/'

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

GEARMAN_SERVERS = ['127.0.0.1']

# TODO: write a windows/posix branch statement to set windows vs. posix paths
OPEN_OFFICE_PATH = 'C:/Program Files/OpenOffice.org 3/program/'
# or
# OPEN_OFFICE_PATH = '/usr/lib/openoffice/program/'

FFMPEG_EXECUTABLE = os.path.normpath(os.path.join(PROJECT_ROOT, 'dist', 'windows', 'ffmpeg', 'bin', 'ffmpeg.exe'))
# or
# FFMPEG_EXECUTABLE = os.path.normpath('/usr/local/bin/ffmpeg')

#####-#####
# Optional external services
#

GOOGLE_ANALYTICS_MODEL = True

# paste your google analytics tracker snipit below
CUSTOM_TRACKER_HTML = ""

# Flickr federated search
# See http://www.flickr.com/services/api/misc.api_keys.html to generate keys
FLICKR_KEY = ''
FLICKR_SECRET = ''

# Artstor federated search
# Set to None if you don't subscribe to ARTstor
ARTSTOR_GATEWAY = None
#ARTSTOR_GATEWAY = 'http://sru.artstor.org/SRU/artstor.htm'

## OPTIONAL External API Keys Settings

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

CLOUDFILES_API_KEY = ''


#####- Authentication Settings -##### #####-##### #####-##### #####-##### #####-##### #####-##### #####-##### #####-###

# By default
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'rooibos.auth.ldapauth.LdapAuthenticationBackend',
    #    'rooibos.auth.mailauth.ImapAuthenticationBackend',
    #    'rooibos.auth.mailauth.PopAuthenticationBackend',
)


# TODO: Test/review ldap functionality and handling with django 1.6
# see http://pythonhosted.org/django-auth-ldap/index.html for alternative ldap scheme?


# By default, video delivery links are created as symbolic links. Some streaming
# servers (e.g. Wowza) don't deliver those, so hard links are required.
HARD_VIDEO_DELIVERY_LINKS = False

additional_settings = [
#    'apps.jmutube.settings_local',
#    'apps.svohp.settings_local',
]

if DEBUG:
    MIDDLEWARE_CLASSES = (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INSTALLED_APPS = (
        'debug_toolbar',
    )

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        #'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        #'debug_toolbar.panels.logger.LoggingPanel',
    )

    DEBUG_TOOLBAR_CONFIG = (
        {
            'INTERCEPT_REDIRECTS': False
        }
    )

######--- CL_DEBUG Stuff ---###### #####-##### #####-##### #####-##### #####-##### #####-##### #####-##### #####-#####

# This will print a fair amount of information helpful for debugging an installation
# if CL_DEBUG = True at the beginning of this file
# see http://blog.dscpl.com.au/2010/03/improved-wsgi-script-for-use-with.html
if CL_DEBUG:
    print '======CL_DEBUG=True=================================\n'
    print "__name__    =", __name__
    print "__file__    =", __file__
    print "os.getpid() =", os.getpid()
    print "os.getcwd() =", os.getcwd()
    print "os.curdir   =", os.path.abspath(os.curdir)
    print "sys.path    =", repr(sys.path)

if CL_DEBUG == 'Full':
    print '=================forks in sys.path==================\n'
    for forks in sys.path:
        print forks
    print '==================sys.modules.keys==================\n'
    print "sys.modules.keys() =", repr(sys.modules.keys())
    print "sys.modules.has_key('rooibos') =", sys.modules.has_key('rooibos')
    if sys.modules.has_key('rooibos'):
        print "sys.modules['rooibos'].__name__ =", sys.modules['rooibos'].__name__
        print "sys.modules['rooibos'].__file__ =", sys.modules['rooibos'].__file__
        print "os.environ['DJANGO_SETTINGS_MODULE'] =", os.environ.get('DJANGO_SETTINGS_MODULE', None)
    print '\n==================end=cl_debug======================\n'


######--- Logging Setup ---###### #####-##### #####-##### #####-##### #####-##### #####-##### #####-##### #####-#####

# set LOGGING_OUTPUT_ENABLED to True to reduce log verbosity
# or False to disable logging
LOGGING_OUTPUT_ENABLED = DEBUG
LOGGING_LOG_SQL = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': DEFAULT_DATA_DIR + "/logs/rooibos.log",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'rooibos': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}

if DEBUG:
    def show_toolbar(request):
        return True
    SHOW_TOOLBAR_CALLBACK = show_toolbar



############# end settings_local #####-##### #####-##### #####-##### #####-##### #####-##### #####-##### #####-#####
