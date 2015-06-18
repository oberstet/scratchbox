import os
from twisted.internet import reactor
import treq

# https://mailgun.com/app/domains/mailing.crossbar.io
auth = ("api", os.environ["MAILGUN_KEY"])
data= {
    "from": "Crossbar.io <no-reply@mailing.crossbar.io>",
    "to": ["tobias.oberstein@tavendo.de"],
    "subject": "Please activate your Crossbar.io account",
    "text": "Please click on the following link ..",
    "html": """To activate your account, please click <a href="http://crossbar.io">here</a>."""
}


def on_success(res):
    print("ok", res)

def on_error(err):
    print("err", err)

def stop(_):
    reactor.stop()

d = treq.post('https://api.mailgun.net/v3/mailing.crossbar.io/messages',
    auth=auth, data=data)

d.addCallbacks(on_success, on_error)
d.addBoth(stop)

reactor.run()
