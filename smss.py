import os
from twilio.rest import Client


account_sid = "AC87f73a0cd7c7eedcd1e933eb7df84e54"
auth_token = "88a47775c4aa0e4d914011c4508c910f"

client = Client(account_sid, auth_token)


message = client.messages.create(
    body="I know where u live, Avni",
    from_="+13252372522",
    to="+49 157 52454992"
)

print(message.sid)
