######################################################################
##
##   Copyright (c) 2013 Tavendo GmbH. All rights reserved.
##   Author(s): Tobias Oberstein
##
######################################################################

## Amazon S3 configuration
##
BUCKET = "webmq"
FILES = ["dist/webmq.exe", "dist/webmqora.exe"]


import sys, os

from boto.s3.connection import S3Connection
from boto.s3.key import Key

conn = S3Connection()
bucket = conn.get_bucket(BUCKET)


def percent_cb(complete, total):
   sys.stdout.write("%d %%\n" % round(100. * float(complete) / float(total)))
   sys.stdout.flush()


for f in FILES:
   filename = os.path.basename(f)
   key = bucket.lookup(filename)
   if key:
      fingerprint = key.etag.replace('"', '')
   else:
      fingerprint = None
      key = Key(bucket, filename)

   fp = str(key.compute_md5(open(f, "rb"))[0])
   fs = os.path.getsize(f)

   if fingerprint != fp:
      print "Uploading file %s (%d bytes, %s MD5) .." % (f, fs, fp)
      key.set_contents_from_filename(f, cb = percent_cb, num_cb = 100)
      key.set_acl('public-read')
   else:
      print "File %s already on S3 and unchanged." % f
