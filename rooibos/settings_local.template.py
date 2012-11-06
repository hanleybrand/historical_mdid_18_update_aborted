import sys, os

######--- Logging and Diagnostics ---######

# Debug should never be true on a production system
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# set LOGGING_OUTPUT_ENABLED to True to reduce log verbosity
# or False to disable logging
LOGGING_OUTPUT_ENABLED = DEBUG
LOGGING_LOG_SQL = False

# CL_DEBUG when set to true this will output useful info to the terminal or logs
# when mdid3 initializes (see CL_DEBUG section near end of file)
CL_DEBUG = True

# TESTING used for running tests to check installation
# set to True before running tests with
#     python manage.py test access converters data federatedsearch \
#         artstor presentation statistics storage userprofile util viewers workers
#
# from this directory (project_root/rooibos/). MDID will not function correctly when Testing = True
TESTING = False

## Directory variables
#   - project & rooibos root will always be correct even if the
#     directory is moved
#   - data_dir defaults to a directory in project root
#     static_dir
#
#  NOTE: any of the computed os.path can be replaced by a string containing an absolute system path
#  e.g.
#      default_data = '/var/local/mdid-data'  # unix path
#  or
#      default_data = 'c:/mdid-scratch/'  # windows path - note forward slashes

project_root = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
rooibos_root = os.path.normpath(os.path.join(os.path.dirname(__file__)))

# default_data defaults to an included directory for convenience and quick setup
# but is unnecessary except as a container for other data directories
# if your infrastructure plan does not call for all application data to be stored in
# a central location you can delete the default_data as long as you change the paths to directories
# inside it.
default_data = os.path.normpath(os.path.join(project_root, 'mdid-data'))
scratch_dir = os.path.normpath(os.path.join(default_data, 'mdid-scratch'))


######--- Web Application settings ---######

### Needed to enable compression JS and CSS files
COMPRESS = True

### Upload Limit is in kilobytes;
UPLOAD_LIMIT = 5242880

MEDIA_URL = '/static/'
MEDIA_ROOT = os.path.normpath(os.path.join(rooibos_root, 'static'))

SCRATCH_DIR = os.path.normpath(os.path.join(default_data, 'mdid-scratch'))
AUTO_STORAGE_DIR = os.path.normpath(os.path.join(default_data, 'mdid-collections'))

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

#  Admins will receive error messages via email when DEBUG = False  above
ADMINS = (
#    ('Your name', 'your@email.example'),
)
MANAGERS = ADMINS

# Theme colors for use in CSS
PRIMARY_COLOR = "rgb(152, 189, 198)"
SECONDARY_COLOR = "rgb(118, 147, 154)"

# Legacy setting for ImageViewer 2 support
SECURE_LOGIN = False

# MDID3 will redirect http requests to the
# port specified using https (use None to disable)
SSL_PORT = None
#SSL_PORT = ':443'

SESSION_COOKIE_AGE = 6 * 3600  # in seconds

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/'

WWW_AUTHENTICATION_REALM = "Please log in to access media from MDID at Your University"

# Add your desktop machine's IP in order to be able to
# view site with information normally restricted to the server console
INTERNAL_IPS = ('127.0.0.1',)

# The Help link in the MDID3 menu bar will go to this url
HELP_URL = 'http://mdid.org/help/'

DEFAULT_LANGUAGE = 'en-us'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# By default, video delivery links are created as symbolic links. Some streaming
# servers (e.g. Wowza) don't deliver those, so hard links are required.
HARD_VIDEO_DELIVERY_LINKS = False

EXPOSE_TO_CONTEXT = ('STATIC_DIR', 'PRIMARY_COLOR', 'SECONDARY_COLOR', 'CUSTOM_TRACKER_HTML', 'ADMINS')



######--- Database Configuration ---######
#

# Settings for MySQL
DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_OPTIONS = {
    'use_unicode': True,
    'charset': 'utf8',
}

# Settings for Microsoft SQL Server (use the appropriate driver setting)
#DATABASE_ENGINE = 'sql_server.pyodbc'
#DATABASE_OPTIONS= {
#    'driver': 'SQL Native Client',             # FOR SQL SERVER 2005
#    'driver': 'SQL Server Native Client 10.0', # FOR SQL SERVER 2008
#    'MARS_Connection': True,
#}

# Settings for all database systems
DATABASE_NAME = 'rooibos'             # Or path to database file if using sqlite3.
DATABASE_USER = 'rooibos'             # Not used with sqlite3.
DATABASE_PASSWORD = 'rooibos'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

DEFAULT_CHARSET = 'utf-8'
DATABASE_CHARSET = 'utf8'



######--- External Interface & API Settings  ---######

# solr must be running for MDID to function properly
SOLR_URL = 'http://127.0.0.1:8983/solr/'

# memcached or couchbase server must be running for MDID to function properly
# see http://memcached.org or http://www.couchbase.com/couchbase-server/overview for details
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# Confirm path of your open office install (needed for PowerPoint import)
#OPEN_OFFICE_PATH = 'C:/Program Files/OpenOffice.org 3/program/'
#OPEN_OFFICE_PATH = '/usr/lib/openoffice.org3/program'

# only change this if you are sure it needs to be done. (it probably doesn't)
GEARMAN_SERVERS = ['127.0.0.1']

# Set to True to use Google Analytics, and paste your tracking code into CUSTOM_TRACKER_HTML
# see https://developers.google.com/analytics/ for details
GOOGLE_ANALYTICS_MODEL = False
CUSTOM_TRACKER_HTML = ""

# a flickr api key is needed for flickr search integration
# see http://www.flickr.com/services/api/misc.api_keys.html for details
FLICKR_KEY = ''
FLICKR_SECRET = ''

# Set ARTSTOR_GATEWAY to None unless you have completed the
# ARTstor Metaserach Agreement with General Counsel and Secretary
# of ARTstor (note: completion will likely take a few weeks)
ARTSTOR_GATEWAY = None
# see
# http://www.artstor.org/what-is-artstor/w-html/features-and-tools-metasearch.shtml
# for details of how to activate ARTstor
# When the agreement is complete uncomment the line below and comment the one above
#ARTSTOR_GATEWAY = 'http://sru.artstor.org/SRU/artstor.htm'




######--- Authentication settings ---######
#   MDID3 supports an internal authentication system as well as LDAP, IMAP and POP authentication
#   Uncomment the appropriate line in AUTHENTICATION_BACKENDS to activate LDAP, IMAP and/or POP
#   and then fill out the appropriate settings section immediately following.
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
#    'rooibos.auth.ldapauth.LdapAuthenticationBackend',
#    'rooibos.auth.mailauth.ImapAuthenticationBackend',
#    'rooibos.auth.mailauth.PopAuthenticationBackend',
)

MIDDLEWARE_CLASSES = (
    'rooibos.auth.middleware.BasicAuthenticationMiddleware',
)

LDAP_AUTH = (
    {
        # LDAP Example
        'uri': 'ldap://ldap.example.edu',
        'base': 'ou=People,o=example',
        'cn': 'cn',
        'dn': 'dn',
        'version': 2,
        'scope': 1,
        'options': {'OPT_X_TLS_TRY': 1},
        'attributes': ('sn', 'mail', 'givenName', 'eduPersonPrimaryAffiliation'),
        'firstname': 'givenname',
        'lastname': 'sn',
        'email': 'mail',
        'bind_user': '',
        'bind_password': '',
    },
    {
        # Active Directory Example
        'uri': 'ldap://ad.example.edu',
        'base': 'OU=users,DC=ad,DC=example,DC=edu',
        'cn': 'sAMAccountName',
        'dn': 'distinguishedName',
        'version': 3,
        'scope': 2, # ldap.SCOPE_SUBTREE
        'options': {
            'OPT_X_TLS_TRY': 1,
            'OPT_REFERRALS': 0,
            },
        'attributes': ('sn', 'mail', 'givenName', 'eduPersonAffiliation'),
        'firstname': 'givenName',
        'lastname': 'sn',
        'email': 'mail',
        'bind_user': 'CN=LDAP Bind user,OU=users,DC=ad,DC=jmu,DC=edu',
        'bind_password': 'abc123',
    },
)

IMAP_AUTH = (
    {
        'server': 'imap.example.edu',
        'port': 993,
        'domain': 'example.edu',
        'secure': True,
    },
)

POP_AUTH = (
    {
        'server': 'pop.gmail.com',
        'port': 995,
        'domain': 'gmail.com',
        'secure': True,
    },
)



######--- License & API Keys ---######



# Make this unique, and don't share it with anybody.
# generate by typing
#     python manage.py generate_secret_key
# in the rooibos directory
# DON'T USE THE ONE BELOW, CHANGE AS SOON AS POSSIBLE
SECRET_KEY = '^t94yw8uwo7afiv#-+)qakzqq@wmo1^6*am%p^8%5rjnl67*-d'

# The Megazine viewer is using a third party component that has commercial
# licensing requirements.  To enable the component you need to enter your
# license key, which is available for free for educational institutions.
# See static/megazine/COPYING.
MEGAZINE_PUBLIC_KEY = ""

# To use a commercial licensed flowplayer, enter your flowplayer key here
# and add the flowplayer.commercial-3.x.x.swf file to the
# rooibos/static/flowplayer directory
# see http://flowplayer.org/download/ for licensing details
FLOWPLAYER_KEY = ""

# MDID uses some Yahoo APIs that require an application key
# You can get one at https://developer.apps.yahoo.com/dashboard/createKey.html
YAHOO_APPLICATION_ID = ""


######--- Wrap up ---######


# This will print a fair amount of information helpful for debugging an installation
# if CL_DEBUG = True at the beginning of this file
# see http://blog.dscpl.com.au/2010/03/improved-wsgi-script-for-use-with.html
if CL_DEBUG:
    print "__name__ =", __name__
    print "__file__ =", __file__
    print "os.getpid() =", os.getpid()
    print "os.getcwd() =", os.getcwd()
    print "os.curdir =", os.path.abspath(os.curdir)
    print "sys.path =" # , repr(sys.path)
    for forks in sys.path:
        print forks
    print "sys.modules.keys() =", repr(sys.modules.keys())
    print "sys.modules.has_key('rooibos') =", sys.modules.has_key('rooibos')
    if sys.modules.has_key('rooibos'):
        print "sys.modules['rooibos'].__name__ =", sys.modules['rooibos'].__name__
        print "sys.modules['rooibos'].__file__ =", sys.modules['rooibos'].__file__
        print "os.environ['DJANGO_SETTINGS_MODULE'] =", os.environ.get('DJANGO_SETTINGS_MODULE', None)

######--- Basic Testing or Custom Apps ---######

if TESTING:
    # if TESTING = True then settings_test.py will be loaded and will undo many settings here
    # for the purpose of testing basic mdid functionality - otherwise, custom apps if any will be loaded
    additional_settings = ['settings_test',]
else:
    # add any custom apps you would like to install here
    additional_settings = [
    #    'apps.jmutube.settings_local',
    #    'apps.svohp.settings_local',
    ]

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'contrib', 'djangologging', 'templates'),
    )