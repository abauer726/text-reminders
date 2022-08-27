from api_authentication import df
from py_imessage import imessage

phone = "4157268044"

if not imessage.check_compatibility(phone):
    print("Not an iPhone")

guid = imessage.send(phone, "Hello World!")

# Let the recipient read the message
