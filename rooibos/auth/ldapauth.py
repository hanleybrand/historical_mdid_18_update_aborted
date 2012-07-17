from django.contrib.auth.models import User
from django.conf import settings
import ldap
import sys, traceback
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
        
        if settings.DEBUG == True:
             logger.debug('start ldap for  %s' % username)
             ldap.set_option(ldap.OPT_DEBUG_LEVEL, 4095)


        for ldap_auth in settings.LDAP_AUTH:

            try:
                l = ldap.initialize(ldap_auth['uri'])
                logging.debug('login request for  %s' % username)
                username = username.strip()
                l.protocol_version = ldap_auth['version']
                for option, value in ldap_auth['options'].iteritems():
                    l.set_option(getattr(ldap, option), value)
                    
                if ldap_auth.get('bind_user'):
                    logger.debug('Bind user binding %s' % username)

#                    testLdap = l.simple_bind_s(ldap_auth['bind_user'],
#                                    ldap_auth.get('bind_password'))
#                    logger.debug('result of bind user binding: %s' % l.result(testLdap))

                    result = l.search_s(ldap_auth['base'],
                                    ldap_auth['scope'],
                                    '%s=%s' % (ldap_auth['cn'], username),
                                    attrlist=[ldap_auth.get('dn', 'dn')])
                    logger.debug(result)
#                    logger.debug(result[0][0])

                    if (len(result) != 1 ):
                        continue
                    dn = result[0][1].get(ldap_auth.get('dn', 'dn'))
                    logger.debug('result[0][1].get(ldap_auth.get(\'dn\', \'dn\') dn is %s' % dn)
                    
                    if type(dn) in (tuple, list):
                        dn = dn[0]
                        logger.debug('dn=dn[0] is %s' % dn)

                    dn = result[0][0]
                    

                    logger.debug('dn = result[0][0] is %s' % dn)
                else:
                    logger.debug('no bu - binding %s' % username)
                    dn = '%s=%s,%s' % (ldap_auth['cn'],
                                       username, ldap_auth['base'])

                    logger.debug('dn from cn=username,base is %s' % dn)
                testLdap = l.simple_bind_s(dn, password)
                #logger.debug('result is %s' % l.result(testLdap))
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
                logging.debug('LDAP error: %s' % error_message)
            except Exception as e:
                logger.debug(traceback.format_exception(*sys.exc_info()))
                raise # reraises the exception
            finally:
                if l:
                    l.unbind_s()
        return None
