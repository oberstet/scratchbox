import datetime
from typing import Optional, List, Dict
from database import BaseTransaction, MapOidPickle, MapStringOid


class Transaction(BaseTransaction):

    users: MapUUIDPickle = MapUUIDFlatbuffer(slot=1, schema='user.fbs')
    idx_users_by_authid: MapStringUUID = MapStringUUID(slot=2)
    idx_users_by_email: MapStringUUID = MapStringUUID(slot=3)

    def attach(self):
        self.users.attach_transaction(self)
        self.idx_users_by_authid.attach_transaction(self)
        self.users.attach_index('idx1', lambda user: user.authid, self.idx_users_by_authid)
        self.idx_users_by_email.attach_transaction(self)
        self.users.attach_index('idx2', lambda user: user.email, self.idx_users_by_email)
