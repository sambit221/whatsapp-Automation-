# importing twilio library after installing it
# client is for accessing the Twilio API.

from twilio.rest import Client

# Replace first parameter with ACCOUNT SID from twilio id
# Replace second parameter with AUTH TOKEN from twilio id
Client = Client("AC535************************","8d*****************************")

# Replace body attribute with the desired automated message
# Replace from attribute with the generated bot whatsapp number (with country code)
# Replace to attribute with the the whatsapp number you want send the automated message (with country code)
message = Client.messages.create(body = " Hello buddy !! ", from_="whatsapp:+141*********", to ="whatsapp:+91*******" )

# after filling all required information execute it
 # it will automatically send message to the given whatsapp number
