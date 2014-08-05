## adjusted from: http://amix.dk/blog/post/19687

import sys
import mimetypes
import email
import time
import types
from datetime import datetime, timedelta

from boto.s3.connection import S3Connection
from boto.cloudfront import CloudFrontConnection


def main(s3_bucket_name, keys=None, days=30):
    s3_conn = S3Connection()

    bucket = s3_conn.get_bucket(s3_bucket_name)

    if not keys:
        keys = bucket.list()

    for key in keys:
        if type(key) == types.StringType:
            key_name = key
            key = bucket.get_key(key)
            if not key:
                print 'Key not found %s' % key_name
                continue

        # Force a fetch to get metadata
        # see this why: http://goo.gl/nLWt9
        key = bucket.get_key(key.name)

        aggressive_headers = _get_aggressive_cache_headers(key, days)
        key.copy(s3_bucket_name, key, metadata=aggressive_headers, preserve_acl=True)

        print 'Updated cache headers to %s days for %s' % (days, key.name)


def _get_aggressive_cache_headers(key, days):
    metadata = key.metadata

    metadata['Content-Type'] = key.content_type

    # HTTP/1.0
    metadata['Expires'] = '%s GMT' %\
        (email.Utils.formatdate(
            time.mktime((datetime.now() +
            timedelta(days=days)).timetuple())))

    # HTTP/1.1
    metadata['Cache-Control'] = 'max-age=%d, public' % (3600 * 24 * days)

    return metadata


if __name__ == '__main__':
    main( sys.argv[1],
          sys.argv[2:] )