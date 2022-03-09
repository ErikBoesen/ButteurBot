import os
import requests
import mebots
import yaledining
import datetime


"""
with open('token.txt', 'r') as f:
    BOT_TOKEN = f.read().strip()
bot = mebots.Bot('butteur_bot', BOT_TOKEN)
"""
dining = yaledining.API()


def butteur_open():
    buttery_id = 'GH'
    meals = dining._get(f'butteries/{buttery_id}/meals',
                        params={'date': datetime.date.today()})
    return len(meals) > 0


def send(text, bot_id):
    url  = 'https://api.groupme.com/v3/bots/post'

    message = {
        'bot_id': bot_id,
        'text': text,
    }
    r = requests.post(url, json=message)

print(butteur_open())

"""
if serving_tenders():
    bot_ids = [instance.id for instance in bot.instances()]
    for bot_id in bot_ids:
        send('It is chicken tenders day today.', bot_id)
"""
