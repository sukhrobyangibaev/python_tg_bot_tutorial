"""
Retrieve information about your bot

Botingiz haqida ma'lumot olish
"""


from pprint import pprint
import requests

TOKEN = '5581179119:AAFd8Da6TQdmTwtGqdn-3QQp2vcsSDnDEms'

response = requests.get('https://api.telegram.org/bot{}/getMe'.format(TOKEN))

pprint(response.json())
