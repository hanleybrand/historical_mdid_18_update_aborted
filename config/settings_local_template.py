import os
import sys

'''-### directory variables ############################################-

        Self set directory paths based on local file locations
        this may or may not be desired in production, but will allow for quick bootstrapping
        note: for this layout, data is stored outside of the config file hierarchy, i.e.
        /var/local/
        |-- mdid
        |   |-- config/
        |   |-- rooibos/
        |   |-- manage.py
        |-- |-- |-- etc.
        |-- mdid-data
        |   |-- collections/
        |   |-- logs/
        |   |-- rooibos/
        ... &c.

        Any path can be made absolute like this:

        ROOIBOS_ROOT = os.path.normpath( '/var/local/mdid/rooibos' ))

'''

# MDID root  (e.g. /var/local/mdid/ )
PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '../'))
# setting for django-extensions
BASE_DIR = PROJECT_ROOT
# the rooibos directory (e.g. /var/local/mdid/rooibos )
ROOIBOS_ROOT = os.path.normpath(os.path.join(PROJECT_ROOT, 'rooibos'))

'''-### Local Data ############################################-'''

# this defines where files will be stored - by default it will be a directory
# called mdid-data that is in the same directory as PROJECT_ROOT (stored outside of the application)
DEFAULT_DATA_DIR = os.path.normpath(os.path.join(PROJECT_ROOT, '../', 'mdid-data/'))
#DEFAULT_DATA_DIR = os.path.normpath(os.path.join(PROJECT_ROOT, '../', 'mdid-data/', 'hacking-mdid3'))
# I'm trying to remember what this is for...
# DEFAULT_CUSTOM_DIR = os.path.normpath(os.path.join(PROJECT_ROOT, '../', 'mdid-data/', 'local_static'))

# scratch_dir is where image resizes & thumbnails are stored
SCRATCH_DIR = os.path.normpath(os.path.join(DEFAULT_DATA_DIR, 'mdid-scratch'))
# storage for files not defined by storage?
# TODO: get better definition for what AUTO_STORAGE_DIR is for
AUTO_STORAGE_DIR = os.path.normpath(os.path.join(DEFAULT_DATA_DIR, 'collections'))

'''### MEDIA settings

    #  Define urls, [en|dis]able asset compression, template locations, etc.

'''
# It should not be necessary to change these
MEDIA_URL = '/media/'
MEDIA_ROOT = DEFAULT_DATA_DIR

# URL append for the admin site -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

### CSS & JavaScript compression (i.e. minification)

# enable compression set to True or False
COMPRESS_ENABLED = False

# this is set in kb
# TODO: is UPLOAD_LIMIT set in kb?
UPLOAD_LIMIT = 1024 * 1024

# Where django templates are loaded from - in general, adding to this is ok - don't remove directories without
TEMPLATE_DIRS = (
    # It is possible to extend django templates (see changes.md) - save them in [mdid root]/templates
    os.path.normpath(os.path.join(PROJECT_ROOT, 'templates')),
    os.path.normpath(os.path.join(ROOIBOS_ROOT, 'templates')),
    os.path.normpath(os.path.join(ROOIBOS_ROOT, 'access', 'templates')),
    os.path.normpath(os.path.join(ROOIBOS_ROOT, 'ui', 'templates')),
    os.path.normpath(os.path.join(ROOIBOS_ROOT, 'contrib', 'google_analytics', 'templates')),
)

'''#-### DEBUG/SETUP/DEVELOPMENT Variables ############################################

    All variables in this section should be False on a production system

    * NOT_WORKING is for disabling functionality on a development system
'''

DEBUG = True
TEMPLATE_DEBUG = True

# Temp variable to selectively disable problematic modules - setting to true will cause errors.
# see below todos for specific modules
# TODO: /rooibos/util/stats_middleware.py - throws errors with django 1.6
NOT_WORKING = False

# CL_DEBUG when set to true this will print info helpful for troubleshooting
# if set to 'Full' instead of True it will print a fair amount of environment info
# when config initializes, including python paths, etc.
CL_DEBUG = True  # or False or 'Full'

# TESTING used for running tests to check installation
# set to True before running tests with
#     python manage.py test access converters data federatedsearch \
#         artstor presentation statistics storage userprofile util viewers workers
#
# or
# from this directory (PROJECT_ROOT/rooibos/).
# MDID will not function correctly when Testing = True
TESTING = False

'''-### Local MDID Settings  ############################################

        Settings in this section allow customization of your MDID installation
        You can put local files in mdid_dj16-data/local_static and
        add reference them like:
        LOGO_URL = os.path.normpath(os.path.join(DEFAULT_CUSTOM_DIR, 'logo.png'))
        FAVICON_URL = os.path.normpath(os.path.join(DEFAULT_CUSTOM_DIR, 'favico.ico'))

'''

LOGO_URL = None
COPYRIGHT = None
TITLE = None

WWW_AUTHENTICATION_REALM = "Please log in to access media from MDID at Your University"
CUSTOM_TRACKER_HTML = ""
SHOW_FRONTPAGE_LOGIN = 'yes'

ADMINS = (
    #    ('Your name', 'your@email.example'),
)
MANAGERS = ADMINS
# accessing mdid_dj16 from any ip listed below will change the following behaviors:
# see debug comments, when DEBUG is True
# debug_toolbar (if installed) will act as if debug=true
INTERNAL_IPS = ('127.0.0.1', 'localhost')

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

# Theme colors for use in CSS
PRIMARY_COLOR = "rgb(152, 189, 198)"
SECONDARY_COLOR = "rgb(118, 147, 154)"

EXPOSE_TO_CONTEXT = ('STATIC_DIR', 'PRIMARY_COLOR', 'SECONDARY_COLOR', 'CUSTOM_TRACKER_HTML', 'ADMINS')

HELP_URL = 'http://sites.jmu.edu/mdidhelp/'

DEFAULT_LANGUAGE = 'en-us'

''' #####-##### Database settings  ############################################-

    Settings for MySQL are included - even test setups with sqlite are probably a bad idea
    see https://docs.djangoproject.com/en/1.6/ref/databases/#oracle-notes for Oracle Setup

'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rooibos',
        'USER': 'rooibos',
        'PASSWORD': 'rooibos',
        # empty string with host & port = default
        # start host with a forward slash with MySQL to connect via a Unix socket, i.e.
        # "HOST": '/var/run/mysql',
        'HOST': 'localhost',  # note IP6 can cause trouble with localhost, using  '127.0.0.1' is a workaround
        'PORT': '',
        # TODO: test CONN_MAX_AGE (throws error if set to None)
        #    lifetime of a database connection, in seconds - 0 is the old behavior,
        #    None = unlimited persistent connections
        # 'CONN_MAX_AGE': 'None',
        'ATOMIC_REQUEST': False,
        'OPTIONS': {
            # change init_command if you want to specify what mysql engine to use
            # 'init_command': 'SET storage_engine=INNODB',
        },
    }
}

DEFAULT_CHARSET = 'utf-8'
DATABASE_CHARSET = 'utf8'

# TODO: Does MS SQL Server still work with django 1.6? Is this testable anywhere?
# see also http://django-mssql.readthedocs.org/en/latest/
# Settings for Microsoft SQL Server (use the appropriate driver setting)
#DATABASE_ENGINE = 'sql_server.pyodbc'
#DATABASE_OPTIONS= {
#    'driver': 'SQL Native Client',             # FOR SQL SERVER 2005
#    'driver': 'SQL Server Native Client 10.0', # FOR SQL SERVER 2008
#    'MARS_Connection': True,
#}
####


#####-##### other apps  ############################################-'''

# Todo: add windows path back
FFMPEG_EXECUTABLE = '/usr/local/bin/ffmpeg'

SOLR_URL = 'http://127.0.0.1:8983/solr/'

# Legacy setting for ImageViewer 2 support
SECURE_LOGIN = False

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/'

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

GOOGLE_ANALYTICS_MODEL = True

FLICKR_KEY = 'fbef6e60837b1fb2d354bceee23409be'
FLICKR_SECRET = 'dae5ccee937924f9'

# Set to None if you don't subscribe to ARTstor
ARTSTOR_GATEWAY = None
#ARTSTOR_GATEWAY = 'http://sru.artstor.org/SRU/artstor.htm'

OPEN_OFFICE_PATH = 'C:/Program Files/OpenOffice.org 3/program/'

GEARMAN_SERVERS = ['127.0.0.1']

# the default 'localhost' may fail in situations where IP6 is in use
RABBITMQ_OPTIONS = {
    'host': '127.0.0.1'
}

'''-### Authentication Settings ############################################-'''

# By default
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'rooibos.auth.ldapauth.LdapAuthenticationBackend',
    #    'rooibos.auth.mailauth.ImapAuthenticationBackend',
    #    'rooibos.auth.mailauth.PopAuthenticationBackend',
)

# TODO: put the default LDAP config back

# TODO: Test/review ldap functionality and handling with django 1.6
# see http://pythonhosted.org/django-auth-ldap/index.html for alternative ldap scheme?

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

'''-### Install optional apps below  ############################################-'''

additional_settings = [
    #    'apps.jmutube.settings_local',
    #    'apps.svohp.settings_local',
]

if DEBUG:
    # apps listed here will be added to the list of installed apps
    INSTALLED_APPS = (
        #'apps.import_presentation',
        #'apps.add_users_from_json',
    )

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    DEBUG_TOOLBAR_CONFIG = (
        {
            #'INTERCEPT_REDIRECTS': False,
            'RENDER_PANELS': True,
        }
    )

'''-### Logging Setup  ############################################-'''

# set LOGGING_OUTPUT_ENABLED to True to reduce log verbosity
# or False to disable logging
LOGGING_OUTPUT_ENABLED = DEBUG
LOGGING_LOG_SQL = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': DEFAULT_DATA_DIR + "/logs/rooibos.log",
            # 'filename': 'rooibos.log',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': DEFAULT_DATA_DIR + "/logs/rooibos.log",
            # 'filename': 'rooibos.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'rooibos': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}

'''-### Basic Testing or Custom Apps  ############################################
To document
'''

'''-### Command Line Debug ############################################-
# set CL_DEBUG ~line:100
# some stuff cribbed from  http://blog.dscpl.com.au/2010/03/improved-wsgi-script-for-use-with.html
'''

if CL_DEBUG:
    print '======CL_DEBUG=True=================================\n'
    print "local set:     ", __name__
    print "settings path: ", __file__
    print '\n===============================\nDirectories\n==============================='
    print 'project path:  ', PROJECT_ROOT
    print 'rooibos path:  ', ROOIBOS_ROOT
    print 'media root:    ', MEDIA_ROOT
    print 'scratch:       ', SCRATCH_DIR
    print 'auto-storage:  ', AUTO_STORAGE_DIR
    print 'log file:      ', LOGGING['handlers']['file']['filename']

if CL_DEBUG == 'Full':
    print "os.getpid() =", os.getpid()
    print "os.getcwd() =", os.getcwd()
    print "os.curdir   =", os.path.abspath(os.curdir)
    print "sys.path    =", repr(sys.path)
    print '=================forks in sys.path==================\n'
    for forks in sys.path:
        print forks, '\n'
    print '==================sys.modules.keys==================\n'
    print "sys.modules.keys() =", repr(sys.modules.keys())
    print "sys.modules.has_key('rooibos') =", sys.modules.has_key('rooibos')
    if sys.modules.has_key('rooibos'):
        print "sys.modules['rooibos'].__name__ =", sys.modules['rooibos'].__name__
        print "sys.modules['rooibos'].__file__ =", sys.modules['rooibos'].__file__
        print "os.environ['DJANGO_SETTINGS_MODULE'] =", os.environ.get('DJANGO_SETTINGS_MODULE', None)
    print '\n==================end=cl_debug======================\n'

