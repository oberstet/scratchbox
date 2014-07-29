import xmlrpclib
from pprint import pprint

client = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')

releases = client.package_releases('autobahn', True)
latest_release = releases[0]

print latest_release

#pprint(client.release_urls("autobahn", latest_release))
pprint(client.release_data("autobahn", latest_release)['downloads'])

#for release in releases:
#   #pprint("{}: {}".format(release, client.release_data("autobahn", release)['downloads']))
#   pprint("{}: {}".format(release, client.release_downloads("autobahn", release)))
   


# downloads_per_release = {}

# total = 0
# for release in releases:
#    cnt = 0
#    for d in client.release_downloads("autobahn", release):
#       cnt += d[1]
#    r = release.split('.')
#    major = int(r[0])
#    minor = int(r[1])
#    release = (major, minor)
#    if not release in downloads_per_release:
#       downloads_per_release[release] = 0
#    downloads_per_release[release] += cnt
#    total += cnt

# for k in reversed(sorted(downloads_per_release.keys())):
#    rel = '.'.join([str(x) for x in list(k)])
#    print("{}: {}".format(rel, downloads_per_release[k]))
