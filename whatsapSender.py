import os
from twilio.rest import Client


client = Client('AC49231a98e681cba3756a59d41ff5900c',
                '25e76d1191904b87df92c3621309e0a4')

from_whatsapp_number = 'whatsapp:+14155238886'

to_whatsapp_number = 'whatsapp:+9720509095295'

client.messages.create(body='anot',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
