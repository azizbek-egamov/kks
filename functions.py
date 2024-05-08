import asyncio
import logging
import sys
import os
import aiohttp
import aiogram
import re

from os import getenv
from aiogram import types
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from config import *
from button import *
from states import *
from sql import *
from throttling import ThrottlingMiddleware
from check_user import joinchat
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove

dp = Dispatcher()

def user_message(message):

    text = message.text
    cid = message.chat.id
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    full_name = message.chat.full_name
    username = message.chat.username
    is_premium = message.from_user.is_premium

    return {
        "text": text,
        "cid": cid,
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name,
        "username": username,
        "is_premium": is_premium,
    }

def file_get_contents(file):
    try:
        with open(file, 'r') as f:
            return(f.read())
    except:
        return "NaN"
    
def file_exists(file):
    if os.path.exists(file):
        return True
    else:
        return False

def clear_put_contents(file, content):
    with open(file, "w") as f:
        f.write(content)
    
def file_put_contents(file, content):
    with open(file, "a") as f:
        f.write(content)
    
def delfile(file):
    try:
        os.remove(file)
        return True
    except FileNotFoundError:
        return True

def phone_check(value):
    ok = "^[+]998([0-9][012345789]|[0-9][125679]|7[01234569])[0-9]{7}$"
    ok1 = "^998([0-9][012345789]|[0-9][125679]|7[01234569])[0-9]{7}$"

    if re.match(ok, value) or re.match(ok1, value):
        return True\
            
print(len(file_get_contents("step/5668945618.txt").split("\n")) == 13)