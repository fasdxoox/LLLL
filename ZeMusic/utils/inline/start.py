from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="⌯ أضفني إلى مجموعتك ⌯",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="⌯ الأوامر ⌯", callback_data="zzzback")],
        [
            InlineKeyboardButton(text="⌯ المطور ⌯", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="⌯ 𝐬𝐨𝐮𝐫𝐜𝐞 𝐬𝐢𝐦𝐚 ⌯", url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="⌯ أضفني إلى مجموعتك ⌯",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="⌯ الأوامر ⌯", callback_data="zzzback")],
        [
            InlineKeyboardButton(text="⌯ المطور ⌯", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="⌯ 𝐬𝐨𝐮𝐫𝐜𝐞 𝐬𝐢𝐦𝐚 ⌯", url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons
