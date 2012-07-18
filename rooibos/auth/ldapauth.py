from django.contrib.auth.models import User
from django.conf import settings
import ldap
from baseauth import BaseAuthenticationBackend
import logging

logger = logging.getLogger('rooibos')
authlog = logging.FileHandler('/var/local/mdid-storage/mdid-scratch/logs/ldap.log')
logFormat = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
authlog.setFormatter(logFormat)
logger.addHandler(authlog)
logger.setLevel(logging.DEBUG)

class LdapAuthenticationBackend(BaseAuthenticationBackend):

    def authenticate(self, username=None, password=None):

    #  broke this out of authenticate def to avoid UnboundLocalError if
    #  the try:s failed but no LDAPErrors were thrown

        # use a bind user to bind & search for a uid
        def bind_userGetDN(username):
            try:
                l.simple_bind_s(ldap_auth['bind_user'],
                    ldap_auth.get('bind_password'))
                result = l.search_s(ldap_auth['base'],
                    ldap_auth['scope'],
                    '%s=%s' % (ldap_auth['cn'], username),
                    attrlist=[ldap_auth.get('dn', 'dn')])
                if len(result) != 1:
                    dn = result[0][1].get(ldap_auth.get('dn', 'dn'))
                if type(dn) in (tuple, list):
                    dn = dn[0]
                
                logger.debug('bind_userGetDN returns dn as: %s' % dn)
                return dn
            except ldap.LDAPError, error_message:
                logger.debug('LDAP error: %s' % error_message)
                raise

        # search for a uid without binding first, return dn
        def no_bind_userGetDN(username):
            # omit bind user logging in
            try:
                result = l.search_s(ldap_auth['base'],
                    ldap_auth['scope'],
                    '%s=%s' % (ldap_auth['cn'], username),
                    attrlist=[ldap_auth.get('dn', 'dn')])
                logger.debug('no_bindGetDN search result: %s' % result)

                dn = result[0][1].get(ldap_auth.get('dn', 'dn'))

                if type(dn) in (tuple, list):
                    dn = dn[0]
                logger.debug('no_bindGetDN returns dn as: %s' % dn)
                return dn
            except ldap.LDAPError, error_message:
                logger.debug('LDAP error: %s' % error_message)
                raise
    

        for ldap_auth in settings.LDAP_AUTH:
    
            l = ldap.initialize(ldap_auth['uri'])
            logger.debug('begin login for %s' % username)
            logger.debug('settings:  %s' % ldap_auth)

            try:
                username = username.strip()
                l.protocol_version = ldap_auth['version']
                for option, value in ldap_auth['options'].iteritems():
                    l.set_option(getattr(ldap, option), value)

                if ldap_auth.get('bind_user'):
                    logger.debug('binduser %s binding' % ldap_auth.get('bind_user') )
                    dn = bind_userGetDN(username)
                elif ldap_auth.get('no_bindGetDN'):
                    dn = no_bind_userGetDN(username)
                    logger.debug('no_bindGetDN set dn to: %s' % dn )

                else:
                    dn = '%s=%s,%s' % (ldap_auth['cn'],
                                       username, ldap_auth['base'])
 
                try:
                    l.simple_bind_s(dn, password)
                    logger.debug('simple_bind_s( %s , ........ )' % dn )
                except ldap.INVALID_DN_SYNTAX, error_message:
                    logger.debug(error_message)

                result = l.search_s(ldap_auth['base'],
                    ldap_auth['scope'],
                    '%s=%s' % (ldap_auth['cn'], username),
                    attrlist=ldap_auth['attributes'])
                if (len(result) != 1):
                    continue
                attributes = result[0][1]
                for attr in ldap_auth['attributes']:
                    if attributes.has_key(attr):
                        if not type(attributes[attr]) in (tuple, list):
                            attributes[attr] = (attributes[attr],)
                    else:
                        attributes[attr] = []
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    user = self._create_user(username,
                        None,
                        ' '.join(attributes[ldap_auth['firstname']]),
                        ' '.join(attributes[ldap_auth['lastname']]),
                        attributes[ldap_auth['email']][0])
                if not self._post_login_check(user, attributes):
                    continue
                return user
            except ldap.LDAPError, error_message:
                logger.debug('LDAP error: %s' % error_message)
            finally:
                if l:
                    l.unbind_s()
        return None
