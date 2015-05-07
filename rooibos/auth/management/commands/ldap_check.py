import getpass

from django.core.management.base import BaseCommand
from django.conf import settings

import ldap

from rooibos.auth.ldapauth import get_dn, user_bind, ldap_init

class Command(BaseCommand):
    help = '''
           Prompts the user for a username and password combination and checks
           that combination with ldap, and offers suggestions on failure.
           It does not check against the actual MDID/django user base, the tool is only
           meant to test   or help diagnose issues with LDAP
           '''

    def handle(self, *args, **options):
        #ldap_auth = settings.LDAP_AUTH[0]
        lo = ldap_init()

        username = raw_input('Enter your username: ')
        password = getpass.getpass()

        print('Connecting to LDAP server...')

        print('Checking if LDAP bind_user setting')
        try:
            if lo.bind_user:
                bind_the_binders = lo.simple_bind_s(lo.bind_user, lo.bind_password)
                print('(bind_user) binding result: %s' % bind_the_binders)
                if bind_the_binders[0] == 97:
                    print('(bind_user) %s binding was successful' % lo.bind_user)
                    dn = get_dn(username)
                    if dn:
                        if type(dn) in (tuple, list):
                            dn = dn[0]
                    user_bind(dn, password)
                else:
                    print('LDAP binding with %s %s was unsuccessful - check bind user/password pair with LDAP admins'
                          % (lo.bind_user, lo.bind_pass))
            else:
                print('settings_LDAP_AUTH[\'bind_user\'] not configured')
                dn = '%s=%s,%s' % (lo.cn, username, lo.base)
        except Exception as e:
            print(e)

        print('attempting to bind dn: %s' % dn)
