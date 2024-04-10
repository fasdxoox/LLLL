import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from ZeMusic import app

@app.on_message(filters.command(["الرابط","/link"], "") & filters.group & ~filters.private)
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("<b>قم برفعي مسؤول في المجموعة أولا ؟</b>")
    await message.reply_text(f"<b>تم إنشاء رابط الدعوة بنجاح :</b>\n {invitelink}")
    
