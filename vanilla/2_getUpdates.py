"""
Method to receive incoming updates

Kiruvchi yangilanishlarni olish usuli

{'ok': True,
 'result': [{'message': {'chat': {'first_name': 'Sukhrob',
                                  'id': 1476403327,
                                  'last_name': 'Yangibaev',
                                  'type': 'private',
                                  'username': 'sukhrobyangibaev'},
                         'date': 1701604765,
                         'from': {'first_name': 'Sukhrob',
                                  'id': 1476403327,
                                  'is_bot': False,
                                  'language_code': 'en',
                                  'last_name': 'Yangibaev',
                                  'username': 'sukhrobyangibaev'},
                         'message_id': 13015,
                         'text': 'a'},
             'update_id': 579989297}]}
"""

from pprint import pprint
import requests

TOKEN = ''

response = requests.get(
    'https://api.telegram.org/bot{}/getUpdates'.format(TOKEN))

pprint(response.json())
