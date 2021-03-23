# http://www.lothar.com/presentations/fxa-rwc2014/
# https://www.youtube.com/watch?v=G16rOGmpBUc

import os
from uuid import UUID
from binascii import b2a_hex
from pprint import pprint
from fxa.core import Client

client = Client('https://api.accounts.firefox.com')
session = client.login('tobias.oberstein@gmail.com', os.environ['FIREFOX_ACCOUNT_PASSWORD'], keys=True)

# pprint(dir(session))
print('uid={}'.format(UUID(session.uid)))

key_a, key_b = session.fetch_keys()
print('keyA=0x{}'.format(b2a_hex(key_a).decode()))
print('keyB=0x{}'.format(b2a_hex(key_b).decode()))
