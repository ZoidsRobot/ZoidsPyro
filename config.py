# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode as jandigantinantierornanges
from distutils.util import strtobool
from os import getenv
from PyroZen.helpers.cmd import cmd

from dotenv import load_dotenv

load_dotenv("config.env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "✮")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/40a0ecc9b7f5083800118.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, I am alive.")
API_HASH = getenv("API_HASH", "a92aed7d74654a563af4b07efbcd88e9")
API_ID = int(getenv("API_ID", "9774346"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "1.1.5@main"
BRANCH = getenv("BRANCH", "main") #don't change
CMD_HANDLER = [".", "?", "!", "*", "-"]
CMD_HNDLR = [".", "?", "!", "*", "-"]
OWNER_ID = getenv("OWNER_ID", "907544310")
BOT_TOKEN = getenv("BOT_TOKEN", "6129975129:AAH9HMHm6wJNEAmK6V6xm8Mxu6cr5jxZe18")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "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")
CHANNEL = getenv("CHANNEL", "zennihhh")
DB_URL = getenv("DATABASE_URL", "postgresql://yqwuprvg:hFh5CemjIwwXAeEPPsbTv_ASZlIl6XrC@salt.db.elephantsql.com/yqwuprvg")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    jandigantinantierornanges("").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "ZennXSupport")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://github.com/BionXP/PyroZen-Userbot")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQAhIHQAmWUPe-Qq0HjL3YsXOyI-tv5QL5jx3b4d7PYR9HlBYaiWydeV4GziWY5WtL6IJ0ZbCvgcYoMY2rvav-yqryw-RA-2ZFJqNfCdgH4frk4pAHiBpS1jC3lvyk9qbtQTE2D0u_N5CT6N2ZfDazh3bCLJ2bY2VBEOz_Je4u1poluqdgmTQB29PFFhSRQfYkziD3A4a4kEX_kOJc5aU0qS1u8hSQEr8yfYRXKyBSrn3QWlYquSm2f6axOjsMJnk745eQ6fNipPgAMgIGsO7vaKnnGPbW4GK_ygrQqsyeA0_dNXVORonkdQrlC11S7nMWgBb8BNYKAaODTTN2Frnkauoi9SfAAAAAA2GAb2AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "BQAhIHQAZURpahfhty6ooaomKQC9JoZtS5472TMoXhcb4MQRhDLn8fRI2RMbCmds6PZvyAeSsihFo2ReZfh8oFoyqSqLwSaSnj_ytsFDc7516X00pNBexxWovSkhHzfoFRIAjn1etcd0kubU1pMMeZ_2fBscdjlEIiPqEeq5Rfi0E2MwrNwU14aBkbWWYTJO05r-NlOmnafJFBMLzUqM3k0BZ82ixbYIfHrFWr4QID0mPXtiivU_J61mrIwI7kbVkaqvuYlrsjI5P18DUGH0qrixlMka89A6wuWiV4BIo4H2ERRJA3N1EZCr5nu2Fv6DM411g6avg3vuJK6G57mReU5r0us9mQAAAAB1WCiKAA")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
STRING_SESSION11 = getenv("STRING_SESSION11", "")
STRING_SESSION12 = getenv("STRING_SESSION12", "")
STRING_SESSION13 = getenv("STRING_SESSION13", "")
STRING_SESSION14 = getenv("STRING_SESSION14", "")
STRING_SESSION15 = getenv("STRING_SESSION15", "")
STRING_SESSION16 = getenv("STRING_SESSION4", "")
STRING_SESSION17 = getenv("STRING_SESSION17", "")
STRING_SESSION18 = getenv("STRING_SESSION18", "")
STRING_SESSION19 = getenv("STRING_SESSION19", "")
STRING_SESSION20 = getenv("STRING_SESSION20", "")
STRING_SESSION21 = getenv("STRING_SESSION21", "")
STRING_SESSION22 = getenv("STRING_SESSION22", "")
STRING_SESSION23 = getenv("STRING_SESSION23", "")
STRING_SESSION24 = getenv("STRING_SESSION24", "")
STRING_SESSION25 = getenv("STRING_SESSION25", "")
STRING_SESSION26 = getenv("STRING_SESSION26", "")
STRING_SESSION27 = getenv("STRING_SESSION27", "")
STRING_SESSION28 = getenv("STRING_SESSION28", "")
STRING_SESSION29 = getenv("STRING_SESSION29", "")
STRING_SESSION30 = getenv("STRING_SESSION30", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
