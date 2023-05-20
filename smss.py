#https://www.twilio.com/console/projects/summary get API


import os
from twilio.rest import Client


account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)


message = client.messages.create(
    body="your text",
    from_="number to send to",
    to="Number to send from (the number you generated at Twilio)"
)

print(message.sid)
