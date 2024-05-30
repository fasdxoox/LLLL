import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from ZeMusic import app
from config import OWNER_ID, LOGGER_ID
import config
from random import  choice, randint

@app.on_message(command(["مطور", "المطور"]))
async def devid(client: Client, message: Message):
    usr = await client.get_chat(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    uid = OWNER_ID
    bio = info.bio
    await app.download_media(usr.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
       
    await message.reply_photo(
        photo="downloads/developer.jpg",
        caption=f"""<b>-› 𝙽𝙰𝙼𝙴 ¦ :{name}\n -› 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 ¦ :@{usrnam}\n -› 𝙸𝙳 ¦ :`{uid}`\n -› 𝙱𝙸𝙾 ¦ :{bio}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(name, url=f"tg://user?id={uid}"),
                ],[
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=config.CHANNEL_LINK),
                ],
            ]
        ),
    )
