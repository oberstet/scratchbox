
# <ul class="nodot">
#   <li><strong>Downloads (All Versions):</strong></li>
#   <li>
#     <span>1582</span> downloads in the last day
#   </li>
#   <li>
#     <span>9493</span> downloads in the last week
#   </li>
#   <li>
#     <span>53291</span> downloads in the last month
#   </li>
# </ul>

import requests, re
from pprint import pprint

r = requests.get('https://pypi.python.org/pypi/autobahn/')

downloads = {}
for k in ['day', 'week', 'month']:
   pat = re.compile(r"<span>(\d*)<\/span> downloads in the last {}".format(k))
   m = pat.search(r.text)
   d = int(m.groups()[0])
   downloads[k] = d

pprint(downloads)