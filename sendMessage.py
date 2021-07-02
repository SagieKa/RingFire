import requests
import datetime
import pywhatkit as kit
from telegram.ext import Updater
# bot = telegram.Bot(token='TOKEN')


def sendMessage(message, adress):
    print("statring sendMessage func..................")
    # send message to telgram
    updater = Updater(
        token='1702864193:AAGj_J3ipAQ3wS0P1a2GEoEnnaAXOx9f9FY', use_context=True)
    updater.bot.sendMessage(chat_id='-519827084', text=message)
    updater.bot.sendMessage(chat_id='-519827084', text=adress)
    updater.bot.sendLocation(chat_id='-519827084',
                             latitude=32.0123111,
                             longitude=34.7947405)
    # *****send_to_whatsapp****
    # now = datetime.datetime.now()
    # hour = now.hour
    # minute = now.minute
    # kit.sendwhatmsg("+972542025665",
    #                 message, hour, minute+1)
