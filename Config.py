import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'LuciferMoringstar_Robot')
API_ID = int(environ['API_ID', '7041911'])
API_HASH = environ['API_HASH', 'abab2561c71e3004a55d4ff9763d5383']
BOT_TOKEN = environ['BOT_TOKEN', '6400207558:AAEy6y7KZZF2LYJ7hc-hL1LL27RvRAbii2U']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

BROADCAST_CHANNEL = int(os.environ.get("BROADCAST_CHANNEL", "-1001956199528"))
ADMIN_ID = set(int(x) for x in os.environ.get("ADMIN_ID", "995086208").split())
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://autofilter:autofilter@cluster0.en2bnta.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST", True))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS', '995086208'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS', '-1002226519917'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '995086208').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('FORCES_SUB')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "-1002102214357").split()]
# MongoDB information
DATABASE_NAME = environ['BOT_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Auto Filter V3**

Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "http://www.omdbapi.com/?i=tt3896198&apikey=4f08a979")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
