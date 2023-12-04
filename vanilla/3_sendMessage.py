"""
Method to send text messages

Matnli xabarlarni yuborish usuli

{'ok': True,
 'result': {'chat': {'first_name': 'Sukhrob',
                     'id': 1476403327,
                     'last_name': 'Yangibaev',
                     'type': 'private',
                     'username': 'sukhrobyangibaev'},
            'date': 1701605371,
            'from': {'first_name': 'testbot',
                     'id': 5581179119,
                     'is_bot': True,
                     'username': 'syr_test_bot'},
            'message_id': 13016,
            'text': 'test text'}}
"""

from pprint import pprint
import requests

TOKEN = ''

params = {'chat_id': 1476403327,
          'text': 'test text'}

response = requests.get(
    'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN),
    params)

pprint(response.json())
