import asyncio
import re
import ast

from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
import pyrogram
from Cluster.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, \
    make_inactive
from info import ADMINS, AUTH_CHANNEL, AUTH_USERS, CUSTOM_FILE_CAPTION, AUTH_GROUPS, P_TTI_SHOW_OFF, IMDB, \
    SINGLE_BUTTON, SPELL_CHECK_REPLY, IMDB_TEMPLATE, CH_FILTER, CH_LINK, IMDB_DELET_TIME, START_TXT, BTN_LOCK_TEXT
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings
from Cluster.users_chats_db import db
from Cluster.ia_filterdb import Media, get_file_details, get_search_results
from Cluster.filters_mdb import (
    del_all,
    find_filter,
    get_filters,
)
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

BUTTONS = {}
SPELL_CHECK = {}
PM_FILTER_MODE = {}

#@Client.on_message(filters.command('pmautofilter'))
#async def fil_mod(client, message):
#      pm_mode_on = ["yes", "on", "true"]
 #     pm_mode_of = ["no", "off", "false"]
#
#      try:
#         args = message.text.split(None, 1)[1].lower()
 #     except:
#         return await message.reply("Command is incomplete.")
#
#      m = await message.reply("Processing...")
#
#      if args in pm_mode_on:
#          PM_FILTER_MODE[str(message.chat.id)] = "True"
#          await m.edit("Auto filter enabled for this chat")
#
#      elif args in pm_mode_of:
#          PM_FILTER_MODE[str(message.chat.id)] = "False"
#          await m.edit("Auto filter disabled for this chat")
#      else:
#          await m.edit("Use: `/pmautofilter on` or `/autofilter off`")
#
@Client.on_message(filters.private & filters.text & filters.incoming)
async def pm_give_filter(client,message):
    group_id = message.chat.id
    name = message.text
 
   # if FILTER_MODE.get(str(message.chat.id)) == "False":
     #   return
   # else:
    await auto_filter(client, message)  

