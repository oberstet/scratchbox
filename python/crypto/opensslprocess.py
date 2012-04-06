######################################################################
##
##   Copyright (c) 2011,2012 Tavendo GmbH. All rights reserved.
##   Author(s): Tobias Oberstein
##
######################################################################

OPENSSL_EXECUTABLE = '/usr/local/bin/openssl'

import hashlib
from twisted.internet import protocol, defer, reactor

try:
   import cStringIO as StringIO
except ImportError:
   import StringIO


class _BackRelay(protocol.ProcessProtocol):
   def __init__(self, deferred, input = None):
      self.deferred = deferred
      self.input = input
      self.s = StringIO.StringIO()
      self.e = StringIO.StringIO()

   def connectionMade(self):
      if self.input:
         #print self.input
         self.transport.write(self.input)
         self.transport.closeStdin()

   def errReceived(self, text):
      #print text
      self.e.write(text)

   def outReceived(self, text):
      #print text
      self.s.write(text)

   def processEnded(self, reason):
      rc = reason.value.exitCode
      if rc == 0:
         if self.deferred is not None:
            self.deferred.callback(self.s.getvalue())
      else:
         #print self.e.getvalue()
         if self.deferred is not None:
            self.deferred.errback((rc, self.e.getvalue()))


def runOpenSSL(args, input = None):
   d = defer.Deferred()
   reactor.spawnProcess(_BackRelay(d, input), OPENSSL_EXECUTABLE, (OPENSSL_EXECUTABLE,)+tuple(args))
   return d


def private_key_pem_to_der(pkey):
   """
   Given a private key (PEM), computes the public key fingerprint.
   """
   d = runOpenSSL(['rsa', '-outform', 'DER', '-pubout'], pkey)
   d.addCallback(lambda res: key_fingerprint(res))
   return d


def generate_rsa_key(length = 1024):
   """
   Generate new RSA key and return [Private Key (PEM), Public Key (PEM), fingerprint).
   """
   d = runOpenSSL(['genpkey', '-algorithm', 'RSA', '-pkeyopt', 'rsa_keygen_bits:%d' % length])
   d.addCallback(lambda res: defer.gatherResults([defer.succeed(res),
                                                  private_to_public(res),
                                                  private_key_pem_to_der(res)], consumeErrors = True))
   return d


def cert_fingerprint(cert):
   """
   Given a x509 certificate in PEM format, compute the certificate SHA1 fingerprint.

   """
   d = runOpenSSL(['x509', '-fingerprint', '-sha1', '-noout'], cert)
   return d.addCallback(lambda res: res[res.find('=') + 1:])


def private_to_public(pubk):
   d = runOpenSSL(['rsa', '-pubout', '-outform', 'pem'], pubk)
   return d



def parseSubject(res):
   # /C=US/ST=NY/L=Somewhere/O=MyOrg/OU=MyDept/CN=fqdn.of.my.host
   info = {}
   z = [x.strip() for x in res.split('/') if x.strip() != ""]
   for k in z:
      i = k.split("=")
      info[i[0]] = i[1]
   minfo = {}
   for i in info:
      if i == 'C':
         minfo['country-name'] = info[i]
      if i == 'ST':
         minfo['state-or-province-name'] = info[i]
      if i == 'L':
         minfo['locality-name'] = info[i]
      if i == 'O':
         minfo['organization-name'] = info[i]
      if i == 'OU':
         minfo['organization-unit-name'] = info[i]
      if i == 'CN':
         minfo['common-name'] = info[i]
   return minfo

def csr_pem_to_text(csr_pem):
   d = runOpenSSL(['req', '-text', '-noout'], csr_pem)
   return d

def csr_pem_to_subject_info(csr_pem):
   d = runOpenSSL(['req', '-subject', '-noout'], csr_pem)
#   d.addCallback(lambda res: defer.succeed(parseSubject(res)))
   # subject=/C=US/ST=NY/L=Somewhere/O=MyOrg/OU=MyDept/CN=fqdn.of.my.host
   d.addCallback(lambda res: parseSubject(res[res.find('=') + 1:]))
   return d

def createSubject(subjectInfo):
   # /C=DE/CN=localhost/O=Internet Widgits Pty Ltd/ST=Some-State
   # '/C=US/ST=NY/L=Somewhere/organizationName=MyOrg/OU=MyDept/CN=fqdn.of.my.host'
   si = {}
   for s in subjectInfo:
      if s == 'country-name':
         si['C'] = subjectInfo[s]
      if s == 'state-or-province-name':
         si['ST'] = subjectInfo[s]
      if s == 'locality-name':
         si['L'] = subjectInfo[s]
      if s == 'organization-name':
         si['O'] = subjectInfo[s]
      if s == 'organization-unit-name':
         si['OU'] = subjectInfo[s]
      if s == 'common-name':
         si['CN'] = subjectInfo[s]
   r = "'/" + "/".join(["%s=%s" % (x[0], x[1]) for x in  si.items()]) + "'"
   return r

def create_csr_pem(subjectkey_pem, subject_info):
   d = runOpenSSL(['req', '-new',
                   '-nodes',
                   '-sha1',
                   '-x509',
                   '-subj', createSubject(subject_info),
                   '-days', '3600'],
      subjectkey_pem)
   return d


def dotted(s):
   ss = ':'.join(s[pos:pos+2] for pos in range(0, len(s), 2))
   return ss.upper() # do NOT change to lower() !

def key_fingerprint(pkey):
   """
   Compute fingerprint for key.
   """
   digest = hashlib.sha1(pkey).hexdigest()
   return dotted(digest)



if __name__ == '__main__':

   def printResult(res):
      print res
      return res

   def printResultAndStop(res):
      print res
      reactor.stop()

   def printError(res):
      (rc, errout) = res.value
      print "ERROR", rc
      print errout
      reactor.stop()

   certPem = open("/home/autobahn/scm/AutobahnPython/examples/echo_tls/keys/server.crt").read()
   privKey = open("/home/autobahn/scm/AutobahnPython/examples/echo_tls/keys/server.key").read()
   csrPem = open("/home/autobahn/scm/AutobahnPython/examples/echo_tls/keys/server.csr").read()

   #d = csr_pem_to_text(csrPem)
   #d.addCallback(printResult)
   #d.addErrback(printError)

#   d = csr_pem_to_subject_info(csrPem)
#   d.addCallback(printResult)
#   d.addErrback(printError)

   d = create_csr_pem(privKey, {'common-name':'localhost',
                                'country-name':'DE',
                                'organization-name': 'Tavendo GmbH'})


   #d = defer.gatherResults([csr_pem_to_text(csrPem), csr_pem_to_subject_info(csrPem)], consumeErrors = False)
   #d.addCallback(lambda res: {'text': res[0], 'subject': createSubject(res[1])})
   d.addCallback(printResult)
   d.addErrback(printError)


   #print certPem
   #d = cert_fingerprint(certPem)
   #d.addCallback(printResult)
   #d.addErrback(printError)

   #print privKey
   #d2 = private_key_pem_to_der(privKey)
   #d2.addCallback(printResult)
   #d2.addErrback(printError)


   #d = generate_rsa_key()
   #d2 = d.addCallback(lambda res: defer.gatherResults([d, private_key_pem_to_der(res)]))
   #d.addCallback(lambda res: printResult(res), private_key_pem_to_der(res))
   #d.addCallback(lambda res: private_key_pem_to_der(printResult(res)))
   #d.addCallback(printResult)
   #d.addErrback(printError)
#   d1.addCallbacks(private_key_pem_to_der, printError)
#   d2 = d1.addCallback(lambda x: private_key_pem_to_der(x))
#   d2 = d1.chainDeferred(private_key_pem_to_der)
   #d2.addCallback(lambda x: key_fingerprintprintResult)

   reactor.run()
