class Auth(object):

    def __init__(self, realm=None, authmethod=None, authid=None, authrole=None, authextra=None):
        self.realm = realm
        self.authmethod = authmethod
        self.authid = authid
        self.authrole = authrole
        self.authextra = authextra

class AuthStore(object):

    def __init__(self, conn, prefix):
        self._conn = conn
        self._prefix = u'/cf/auth'

    def get_auth_for_wampcra(self, realm, authid):
        etcd_key = u'{}/wampcra/{}/{}'.format(self._prefix, realm, authid)
        auth = {
          u'secret': u'prq7+YkJ1/KlW1X0YczMHw==',
          u'role': u'frontend',
          u'salt': u'salt123',
          u'iterations': 100,
          u'keylen': 16
        }
        return defer.success(auth)

    def get_auth_for_cryptosign(self, pubkey):
        etcd_key = u'{}/cryptosign/{}'.format(self._prefix, pubkey)
        etcd_auth = {}
        auth = {
           u'pubkey': pubkey,
           u'realm': etcd_auth[u'realm'],
           u'authid': etcd_auth[u'authid'],
           u'role': etcd_auth[u'role'],
           u'extra': etcd_auth[u'extra'],
           u'cache': False
        }
        return defer.success(auth)

    def set_auth_for_cryptosign(self, pubkey, realm=None, role=None, authid=None):
        """
        """

    def get_auth_for_tls(self, fingerprint):
        """
        When the client is authenticating using WAMP-TLS, lookup the complete
        dynamic authentication information given a client TLS certificate fingerprint.

        :returns: Dictionary with authentication info, eg {'authid': .., 'authrole': ..}
        :rtype: dict
        """
        etcd_key = u'{}/tls/{}'.format(self._prefix, fingerprint)
        return defer.success(auth)

# authenticator: authmethod, authid -> realm, authid, authrole, authextra
# proxy:         realm, authrole -> transport
