#https://www.twilio.com/console/projects/summary get API


import os
from twilio.rest import Client


account_sid = "AC87f73a0cd7c7eedcd1e933eb7df84e54"
auth_token = "88a47775c4aa0e4d914011c4508c910f"

client = Client(account_sid, auth_token)


message = client.messages.create(
    body="your text",
    from_="number to send to",
    to="Number to send from (the number you generated at Twilio)"
)

print(message.sid)
