"""
Retrieve information about your bot

Botingiz haqida ma'lumot olish

{'ok': True,
 'result': {'can_join_groups': True,
            'can_read_all_group_messages': False,
            'first_name': 'testbot',
            'id': 5581179119,
            'is_bot': True,
            'supports_inline_queries': True,
            'username': 'syr_test_bot'}}
"""


from pprint import pprint
import requests

TOKEN = ''

response = requests.get('https://api.telegram.org/bot{}/getMe'.format(TOKEN))

pprint(response.json())
