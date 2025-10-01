from dotenv import load_dotenv

load_dotenv()  # This will load the variables from .env into os.environ

import os


class BOT:
    """
    TOKEN: Bot token generated from @BotFather
    """
    TOKEN = os.environ.get("TOKEN", "7733732635:AAG1GFhxe4qDUH8KH57J5DnntMlQwc4hVic")


class API:
    """
    HASH: Telegram API hash from https://my.telegram.org
    ID = Telegram API ID from https://my.telegram.org
    """
    HASH = os.environ.get("API_HASH", "c16b13b73c2f2473b8e3cbcf2ab1d200")
    ID = int(os.environ.get("API_ID", 24638343))


class OWNER:
    """
    ID: Owner's user id, get it from @userinfobot
    """
    ID = int(os.environ.get("OWNER", 6272165202))


class CHANNEL:
    """
    ID: Telegram Channel ID where the bot will post automatically
    """
    ID = int(os.environ.get("CHANNEL_ID", -1002983976336))


class WEB:
    """
    PORT: Specific port no. on which you want to run your bot, DON'T TOUCH IT IF YOU DON'T KNOW WHAT IS IT.
    """
    PORT = int(os.environ.get("PORT", 8000))
