######################################################################
##
##   Copyright (c) 2011,2012 Tavendo GmbH. All rights reserved.
##   Author(s): Tobias Oberstein
##
######################################################################

import hashlib, datetime, binascii, os

from M2Crypto import RSA, BIO, EVP, X509, BN, m2


def x509name_from_info(info):
   """
   Create X509 name object from info dictionary.
   """
   name = X509.X509_Name()
   if info.has_key("common-name") and type(info["common-name"]) in [str, unicode]:
      name.CN = info["common-name"].encode("utf8")
   if info.has_key("country-name") and type(info["country-name"]) in [str, unicode]:
      name.C = info["country-name"].encode("utf8")
   if info.has_key("state-or-province-name") and type(info["state-or-province-name"]) in [str, unicode]:
      name.ST = info["state-or-province-name"].encode("utf8")
   if info.has_key("locality-name") and type(info["locality-name"]) in [str, unicode]:
      name.L = info["locality-name"].encode("utf8")
   if info.has_key("organization-name") and type(info["organization-name"]) in [str, unicode]:
      name.O = info["organization-name"].encode("utf8")
   if info.has_key("organization-unit-name") and type(info["organization-unit-name"]) in [str, unicode]:
      name.OU = info["organization-unit-name"].encode("utf8")
   if info.has_key("email-address") and type(info["email-address"]) in [str, unicode]:
      name.Email = info["email-address"].encode("utf8")
   return name


def info_from_x509name(name):
   """
   Create info dictionary from X509 name object.
   """
   info = {}
   info["common-name"] = name.CN
   info["country-name"] = name.C
   info["state-or-province-name"] = name.ST
   info["locality-name"] = name.L
   info["organization-name"] = name.O
   info["organization-unit-name"] = name.OU
   info["email-address"] = name.Email
   return info


def dotted(s):
   ss = ':'.join(s[pos:pos+2] for pos in range(0, len(s), 2))
   return ss.upper() # do NOT change to lower() !


def key_fingerprint(pkey):
   """
   Compute fingerprint for key.
   """
   digest = hashlib.sha1(pkey.as_der()).hexdigest()
   return dotted(digest)


def cert_fingerprint(cert):
   """
   Compute fingerprint for certificate.
   """
   digest = cert.get_fingerprint(md = "sha1")
   return dotted(digest)


def generate_rsa_key(length = 1024):
   """
   Generate new RSA key and return (PEM, fingerprint).
   """
   key = RSA.gen_key(length, m2.RSA_F4, callback = lambda: None)

   kmem = BIO.MemoryBuffer()
   key.save_key_bio(kmem, cipher = None)
   keypem = kmem.getvalue()

   pub_kmem = BIO.MemoryBuffer()
   key.save_pub_key_bio(pub_kmem)
   pub_keypem = pub_kmem.getvalue()

   pkey = EVP.PKey(md = "sha1")
   pkey.assign_rsa(key)

   fingerprint = key_fingerprint(pkey)

   return (keypem, pub_keypem, fingerprint)


def create_certificate(issuerPrivKey,
                       issuerInfo,
                       subjectPubKey,
                       subjectInfo,
                       validForDays,
                       serial,
                       version = 0,
                       hash = 'sha1'):
   """
   Create a certificate and return certificate (PEM, text, fingerprint).
   """

   ikey = RSA.load_key_bio(BIO.MemoryBuffer(issuerPrivKey))
   if ikey.check_key() != 1:
      raise Exception("invalid issuer RSA key")
   p_ikey = EVP.PKey(md = hash)
   p_ikey.assign_rsa(ikey)

   skey = RSA.load_pub_key_bio(BIO.MemoryBuffer(subjectPubKey))
   if skey.check_key() != 1:
      raise Exception("invalid subject RSA key")
   p_skey = EVP.PKey(md = hash)
   p_skey.assign_rsa(skey)

   cert = X509.X509()
   cert.set_pubkey(p_skey)

   issuer = x509name_from_info(issuerInfo)
   cert.set_issuer(issuer)

   subject = x509name_from_info(subjectInfo)
   cert.set_subject(subject)

   notBefore = m2.x509_get_not_before(cert.x509)
   notAfter = m2.x509_get_not_after(cert.x509)
   m2.x509_gmtime_adj(notBefore, 0)
   m2.x509_gmtime_adj(notAfter, 60 * 60 * 24 * validForDays)

   cert.set_serial_number(serial)
   cert.set_version(version)

   cert.sign(p_ikey, hash)
   return (cert.as_pem(), cert.as_text(), cert_fingerprint(cert))


def create_selfsigned_certificate(entityPrivKey,
                                  entityInfo,
                                  validForDays,
                                  serial,
                                  version = 0,
                                  hash = 'sha1'):
   """
   Create a self-signed certificate and return certificate (PEM, text, fingerprint).
   """

   ekey = RSA.load_key_bio(BIO.MemoryBuffer(entityPrivKey))
   ekey_pub_mem = BIO.MemoryBuffer()
   ekey.save_pub_key_bio(ekey_pub_mem)
   ekey_pub_pem = ekey_pub_mem.getvalue()

   return create_certificate(entityPrivKey,
                             entityInfo,
                             ekey_pub_pem,
                             entityInfo,
                             validForDays,
                             serial,
                             version,
                             hash)


def create_certificate_signing_request(subjectPrivKey,
                                       subjectInfo,
                                       version = 0,
                                       hash = 'sha1'):
   """
   Create a certificate signing request (CSR) and return CSR in PEM and text
   formats.

   :param subjectPrivKey: Subject private RSA key in PEM format.
   :type subjectPrivKey: str
   :param subjectInfo: Subject information.
   :type subjectInfo: dict
   :param version: CSR version.
   :type version: int
   :param hash: CSR signing hash, one of 'sha1', 'sha256', ..
   :type hash: str
   :returns tuple -- (CSR in PEM format, CSR as text).
   """

   skey = RSA.load_key_bio(BIO.MemoryBuffer(subjectPrivKey))
   if skey.check_key() != 1:
      raise Exception("invalid subject RSA key")
   p_skey = EVP.PKey(md = hash)
   p_skey.assign_rsa(skey)

   csr = X509.Request()
   csr.set_version(version)
   csr.set_pubkey(p_skey)

   subject = x509name_from_info(subjectInfo)
   csr.set_subject(subject)
   csr.sign(p_skey, hash)
   return (csr.as_pem(), csr.as_text())


def unpack_certificate(certificatePem):
   """
   Unpack X509 PEM-encoded certificate.

   :param certificatePem: PEM encoded X509 certificate.
   :type certificatePem: str
   :returns dict -- Detailed information from the certificate.
   """

   cert = X509.load_cert_bio(BIO.MemoryBuffer(certificatePem))
   cert_pkey_fingerprint = key_fingerprint(cert.get_pubkey())

   res = {}

   ## we include the reserialized PEM encoding (which in principle
   ## should be identical to certificatePem .. but who knows .. this
   ## is x509 crap)
   res["pem"] = cert.as_pem()
   res["text"] = cert.as_text()
   res["fingerprint"] = cert_fingerprint(cert)

   ## we convert this to dotted hex, since the version
   ## might be a unsigned long (8 bytes) which i.e. JavaScript
   ## can't consume
   serial = "0x%x" % cert.get_serial_number()
   res["serial"] = dotted(serial[2:])

   res["version"] = cert.get_version()
   res["issuer"] = info_from_x509name(cert.get_issuer())
   res["subject"] = info_from_x509name(cert.get_subject())

   now = datetime.datetime.utcnow()

   ## we need to strip of timezone info, since we cannot compare
   ## datetime with/without tzinfo, and Python utcnow() for strange
   ## reasons does not contain tzinfo. The date returned from cert
   ## should be UTC anyway.
   before = cert.get_not_before().get_datetime()
   before = before.replace(tzinfo = None)
   after = cert.get_not_after().get_datetime()
   after = after.replace(tzinfo = None)

   UTC_TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
   res["not-valid-before"] = before.strftime(UTC_TIMESTAMP_FORMAT)
   res["not-valid-after"] = after.strftime(UTC_TIMESTAMP_FORMAT)
   res["valid-now"] = before <= now and now <= after

   pubkey = cert.get_pubkey()

   res["public-key"] = {"length": pubkey.size() * 8,
                        "fingerprint": key_fingerprint(pubkey)}

   res["is-selfsigned"] = True if cert.verify(pubkey) == 1 else False
   return res


import cStringIO

def cipher_filter(cipher, s):
   inf = cStringIO.StringIO(s)
   outf = cStringIO.StringIO()
   while 1:
      buf = inf.read()
      if not buf:
         break
      outf.write(cipher.update(buf))
   outf.write(cipher.final())
   return outf.getvalue()


PADDING = {'none': RSA.no_padding,
           'pkcs1': RSA.pkcs1_padding,
           'pkcs1_oaep': RSA.pkcs1_oaep_padding,
           'sslv23': RSA.sslv23_padding}

def encrypt_and_sign(msg,
                     senderPrivPem,
                     receiverPubPem,
                     hash = 'sha256',
                     cipher = 'aes_256_cbc',
                     padding = 'pkcs1_oaep'):

   padding = PADDING[padding]

   key_len = int(cipher.split("_")[1])
   key = os.urandom(key_len/8)
   iv = os.urandom(key_len/8)
   c = EVP.Cipher(alg = cipher, key = key, iv = iv, op = m2.encrypt)
   pmsg = cipher_filter(c, msg)

   rkey = RSA.load_pub_key_bio(BIO.MemoryBuffer(receiverPubPem))
   emsg = rkey.public_encrypt(key + iv, padding)

   md = EVP.MessageDigest(hash)
   md.update(pmsg)
   md.update(emsg)
   digest = md.digest()

   skey = RSA.load_key_bio(BIO.MemoryBuffer(senderPrivPem))
   sig = skey.sign(digest, hash)

   return (binascii.b2a_base64(pmsg).strip(),
           binascii.b2a_base64(emsg).strip(),
           binascii.b2a_base64(sig).strip())


def verify_and_decrypt(pmsg,
                       emsg,
                       sig,
                       senderPubPem,
                       receiverPrivPem,
                       hash = 'sha256',
                       cipher = 'aes_256_cbc',
                       padding = 'pkcs1_oaep'):

   padding = PADDING[padding]

   pmsg = binascii.a2b_base64(pmsg)
   emsg = binascii.a2b_base64(emsg)
   sig = binascii.a2b_base64(sig)

   key_len = int(cipher.split("_")[1])
   md = EVP.MessageDigest(hash)
   md.update(pmsg)
   md.update(emsg)
   digest = md.digest()

   skey = RSA.load_pub_key_bio(BIO.MemoryBuffer(senderPubPem))
   if not skey.verify(digest, sig, hash):
      raise Exception("could not verify signature")

   rkey = RSA.load_key_bio(BIO.MemoryBuffer(receiverPrivPem))

   kv = rkey.private_decrypt(emsg, padding)
   key = kv[0:key_len/8]
   iv = kv[key_len/8:]

   c = EVP.Cipher(alg = cipher, key = key, iv = iv, op = m2.decrypt)
   msg = cipher_filter(c, pmsg)

   return msg



if __name__ == '__main__':

   ## generate new RSA key and self-signed certificate
   ##
   (keypem, pub_keypem, fingerprint) = generate_rsa_key()
   certPem = create_selfsigned_certificate(keypem, {'common-name': 'example.com'}, 360, 1)
   res = unpack_certificate(certPem[0])
   print res['is-selfsigned']
   print res['text']


   ## simple test for: encrypt msg with fresh symmetric key/cipher,
   ## plus encrypting symmetric key, and signing everything with RSA

   msg = "Hello, world!!" * 100

   (tx_keypem, tx_pub_keypem, _) = generate_rsa_key(1024)
   (rx_keypem, rx_pub_keypem, _) = generate_rsa_key(1024)

   (pmsg, emsg, sig) = encrypt_and_sign(msg, tx_keypem, rx_pub_keypem)
   msg2 = verify_and_decrypt(pmsg, emsg, sig, tx_pub_keypem, rx_keypem)

   if msg == msg2:
      print "encrypt/decrypt roundtrip : OK"
   else:
      print "encrypt/decrypt roundtrip : FAIL"
