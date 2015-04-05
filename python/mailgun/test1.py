import os
import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/mailing.crossbar.io/messages",
        auth=("api", os.environ["MAILGUN_KEY"]),
        data={"from": "Excited User <mailgun@mailing.crossbar.io>",
              "to": ["bar@example.com", "tobias.oberstein@tavendo.de"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

send_simple_message()
