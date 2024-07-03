import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '22827872'))
API_HASH = environ.get('API_HASH', 'a9e30c6a4784192f919406d19ba44e80')
BOT_TOKEN = environ.get('BOT_TOKEN', '7127950400:AAEe7bwRcZxM4ZD6A2hxp1_vq1NiUzjqqkY')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6615966362').split()]
USERNAME = environ.get('USERNAME', 'https://t.me/renoji')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002071398722'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/hhjjjvvhhhggg')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002028049401').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Princess:Princess55@princess.xgq7smm.mongodb.net/?retryWrites=true&w=majority")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://Princess6:Princess66@princess.xgq7smm.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Princess")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Aks')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1001929995223'))
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/901c940e1e0f64e0fe6ac.jpg')

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002032456077'))
URL = environ.get('URL', '')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002047161941'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/how_to_download_channel/17")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "a37bd0e6190b14ff1c189e54dbaab94fe5a72bbe")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "zipshort.net")
SHORTENER_API2 = environ.get("SHORTENER_API2", "7307594e5e1df8e8f21361a5ed2bf72f76c4ece3")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "publicearn.com")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "600"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1002132409575')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002147420607'))

# hastags request features
request_channel = environ.get('REQUEST_CHANNEL', '-1002132202139')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None

# bot settings
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
