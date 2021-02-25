import os
from twilio.rest import Client


client = Client()
from_whatsapp_number='whatsapp:+917004518207'
to_whatsapp_number='whatsapp:' + os.environ['MY_PHONE_NUMBER']


client.messages.create(body='hello i am ankit',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)