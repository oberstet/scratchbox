import lmdb
import datetime
from typing import Optional, List, Dict

import dbutil


class User(object):

    oid: int
    name: str
    authid: str
    email: str
    birthday: datetime.date
    is_friendly: bool
    tags: Optional[List[str]]
    ratings: Dict[str, float] = {}
    friends: List[int] = []
    referred_by: int = None


class Transaction(dbutil.BaseTransaction):
    """
    Definition of application database schema
    """

    users: dbutil.MapOidPickle = dbutil.MapOidPickle(slot=1)
    """
    Maps user OID to user object (in pickle format).
    """

    users_by_authid: dbutil.MapStringOid = dbutil.MapStringOid(slot=2)
    """
    Maps user authid to user OID.
    """

    users_by_email: dbutil.MapStringOid = dbutil.MapStringOid(slot=3)
    """
    Maps user email to user OID.
    """

    def attach(self):
        # table: oid-user -> user
        self.users.attach(self)

        # index: authid -> oid-user
        self.users_by_authid.attach(self)
        self.users.set_index('idx1', lambda user: user.authid, self.users_by_authid)

        # index: email -> oid-user
        self.users_by_email.attach(self)
        self.users.set_index('idx2', lambda user: user.email, self.users_by_email)
