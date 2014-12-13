## Update a Route53 for a dynamically changing IP read from
## a DD-WRT router
##

## CONFIGURATION

## This script reads AWS credentials from $HOME/.boto
## This file should contain something like:
#
# [Credentials]
# aws_access_key_id = XXXX....
# aws_secret_access_key = XXXXX...

## "tavendo.de" zone on Router 53
AWS_R53_ZONE = "Z3PRGPYIIX4JFU"

## record to update
AWS_R53_ZONE_RECORD = "office.tavendo.de"

## DD-WRT
DDWRT_ROUTER_STATUS_PAGE = "http://192.168.1.1/"

## END OF CONFIGURATION


import sys
import re
import urllib2
from boto import route53
from boto.route53.record import ResourceRecordSets


def get_public_ip():
   html = urllib2.urlopen(DDWRT_ROUTER_STATUS_PAGE).read()
   p = re.compile(r"IP\: ([0-9\.]*)\</span")
   f = p.search(html)
   if f and len(f.groups()) > 0:
      ip = f.groups()[0]
      return ip
   else:
      print("Could not scrape IP address in router status page")
      sys.exit(1)


wan_ip = get_public_ip()
print("Current WAN IP on Router: {}".format(wan_ip))

r53 = route53.connect_to_region('universal')
rec = r53.get_all_rrsets(AWS_R53_ZONE, 'A', AWS_R53_ZONE_RECORD, maxitems = 1)[0]
cur_ip =  str(rec.resource_records[0])

if cur_ip == wan_ip:
   print("Nothing to update - current IP {} configured for {} is still correct.".format(cur_ip, AWS_R53_ZONE_RECORD))
else:
   print("IP for {} needs to be updated from {} to {} ...".format(AWS_R53_ZONE_RECORD, cur_ip, wan_ip))

   try:
      r53rr = ResourceRecordSets(r53, AWS_R53_ZONE)
      d_record = r53rr.add_change('DELETE', AWS_R53_ZONE_RECORD, "A", 60)
      d_record.add_value(cur_ip)
      c_record = r53rr.add_change('CREATE', AWS_R53_ZONE_RECORD, 'A', 60)
      c_record.add_value(wan_ip)
      r53rr.commit()
   except Exception as e:
      print("Failed to update zone record: {}".format(e))
      sys.exit(1)

   print("Zone record updated!")
