import datetime
from typing import Optional

class User(object):

    def __init__(self, oid, name, authid, email, birthday=None, is_friendly=True, tags=None, ratings=None, friends=None):
        self.oid = oid
        self.name = name
        self.authid = authid
        self.email = email
        self.birthday = birthday
        self.is_friendly = is_friendly
        self.tags = tags or []
        self.ratings = ratings or {}
        self.friends = friends or []
        self.referred_by: Optional[User] = None


users = []

user = User(oid=1,
            name='Homer Simpson',
            authid='homer',
            email='homer.simpson@example.com',
            birthday=datetime.date(1950, 12, 24),
            is_friendly=True,
            tags=['relaxed', 'beerfan'])
users.append(user)

user = User(oid=2,
            name='Crocodile Dundee',
            authid='crocoboss',
            email='croco@example.com',
            birthday=datetime.date(1960, 2, 4),
            is_friendly=False,
            tags=['red', 'yellow'])
users.append(user)

user = User(oid=3,
            name='Foobar Space',
            authid='foobar',
            email='foobar@example.com',
            birthday=datetime.date(1970, 5, 7),
            is_friendly=True,
            tags=['relaxed', 'beerfan'])
users.append(user)
