import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(
  command(["مطور اساسي","مطور السورس","مبرمج السورس","المطور الاساسي", "مطور ثانوي", "المطور الثانوي"])
)
async def huhh(client: Client, message: Message):
    dev_id = config.OWNER_ID
    dev = await client.get_users(dev_id)
    name = dev.first_name
    usrnam = dev.username
    bio = dev.bio
    await app.download_media(dev.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
   
    await message.reply_photo(
        photo="downloads/developer.jpg",
        caption=f"""<b>⌯ 𝙽𝙰𝙼𝙴 :</b> <a href='https://t.me/{usrnam}'>{name}</a>\n\n<b>⌯ 𝙱𝙸𝙾  :</b> {bio}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         name, url=f"https://t.me/{usrnam}"), 
                 ],[
                   InlineKeyboardButton(
                        "『 𝙺𝙸𝙽𝙶 𝚂𝙾𝚄𝚁𝙲𝙴 』", url=f"https://t.me/EF_19"),
                ],

            ]

        ),

    )
