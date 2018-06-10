import datetime
from typing import Optional, List, Dict
from database import BaseTransaction, MapOidPickle, MapStringOid


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


class Transaction(BaseTransaction):
    """
    Definition of application database schema
    """

    users: MapOidPickle = MapOidPickle(slot=1)
    """
    Maps user OID to user object (in pickle format).
    """

    idx_users_by_authid: MapStringOid = MapStringOid(slot=2)
    """
    Maps user authid to user OID.
    """

    idx_users_by_email: MapStringOid = MapStringOid(slot=3)
    """
    Maps user email to user OID.
    """

    def attach(self):
        # table: oid-user -> user
        self.users.attach_transaction(self)

        # index: authid -> oid-user
        self.idx_users_by_authid.attach_transaction(self)
        self.users.attach_index('idx1', lambda user: user.authid, self.idx_users_by_authid)

        # index: email -> oid-user
        self.idx_users_by_email.attach_transaction(self)
        self.users.attach_index('idx2', lambda user: user.email, self.idx_users_by_email)
