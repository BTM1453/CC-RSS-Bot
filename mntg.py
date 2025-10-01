from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import OWNER


class TEXT:
    START = """
<b>Hi {}, I'm The Powerfull Personal Bot.\n\n Don't Waste Your Time </b>[ <i> Made With Love By @CC_Telegram_Helper_Bot </i> ].
"""
    DEVELOPER = "Developer 💀"
    UPDATES_CHANNEL = "Updates Channel ❣️"
    SOURCE_CODE = "🔗 Source Code"


class INLINE:
    START_BTN = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(TEXT.DEVELOPER, url="https://t.me/CC_Telegram_Helper_Bot"),
            ],
            [
                InlineKeyboardButton(
                    TEXT.UPDATES_CHANNEL, url="https://t.me/+SYC6eszIPyIxMjM1"
                ),
            ],
            [
                InlineKeyboardButton(
                    TEXT.SOURCE_CODE,
                    url="https://t.me/TBM_Bot_Updates",
                ),
            ],
        ]
    )
