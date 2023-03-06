# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import os
import time
from platform import python_version

from pyrogram import Client
from pyrogram import __version__ as versipyro
from pyrogram import filters
from pyrogram.types import Message
from telegraph import exceptions, upload_file

from config import BOT_VER, CHANNEL
from config import CMD_HANDLER as cmd
from config import GROUP
from PyroZen import CMD_HELP, StartTime
from PyroZen.helpers.basic import edit_or_reply
from PyroZen.helpers.PyroHelpers import ReplyCheck
from PyroZen.helpers.SQL.globals import gvarstatus
from PyroZen.helpers.tools import convert_to_image
from PyroZen.utils import get_readable_time
from PyroZen.utils.misc import restart

from .help import add_command_help

modules = CMD_HELP
alive_logo = (
    gvarstatus("ALIVE_LOGO") or ""
)
emoji = gvarstatus("ALIVE_EMOJI") or "✮"
alive_text = gvarstatus("ALIVE_TEKS_CUSTOM") or "✪ 𝙸'𝙼 𝙰𝙻𝙸𝚅𝙴 𝚃𝙾𝙳 ✪"

@Client.on_message(filters.command(["ZOIDs", "alive"], cmd) & filters.me)
async def alive(client: Client, message: Message):
    xx = await edit_or_reply(message, "🤖")
    await asyncio.sleep(2)
    send = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    uptime = await get_readable_time((time.time() - StartTime))
    man = (
        f"『 ZOIDs-Userbot 』\n\n"
        f"<b>{alive_text}</b>\n\n"
        f"┏━━━━━━━━━━━━━━━━━━━━━┓\n"
        f"┠➣ <b>Master :</b> {client.me.mention} \n"
        f"┠➣ <b>Modules :</b> <code>{len(modules)} Modules</code> \n"
        f"┠➣ <b>Bot Version :</b> <code>{BOT_VER}</code> \n"
        f"┠➣ <b>Python Version :</b> <code>{python_version()}</code> \n"
        f"┠➣ <b>Pyrogram Version :</b> <code>{versipyro}</code> \n"
        f"┠➣ <b>Bot Uptime :</b> <code>{uptime}</code>\n"
        f"┗━━━━━━━━━━━━━━━━━━━━━┛\n\n"
        f"    『 [𝗦𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/{GROUP}) | [𝗖𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/{CHANNEL}) | [𝗢𝘄𝗻𝗲𝗿](tg://user?id={client.me.id}) 』"
    )
    try:
        new_message = await send(
            message.chat.id,
            caption=man,
            reply_to_message_id=ReplyCheck(message),
        )
        await asyncio.gather(
            await xx.delete(),
            await asyncio.sleep(20),
            await client.delete_messages(chat_id=message.chat.id, message_ids=new_message.id),
        )
    except BaseException as e:
         print(f"Error Requests: {e}")
        pass
        return 
    await xx.edit_text(man, disable_web_page_preview=True)
        
@Client.on_message(filters.command("setalivelogo", cmd) & filters.me)
async def setalivelogo(client: Client, message: Message):
    try:
        import PyroZen.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    Man = await edit_or_reply(message, "`Processing...`")
    link = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await Man.edit(f"**ERROR:** `{exc}`")
            os.remove(m_d)
            return
        link = f"https://telegra.ph/{media_url[0]}"
        os.remove(m_d)
    sql.addgvar("ALIVE_LOGO", link)
    await Man.edit(
        f"**Berhasil Mengcustom ALIVE LOGO Menjadi {link}**",
        disable_web_page_preview=True,
    )
    restart()


@Client.on_message(filters.command("setalivetext", cmd) & filters.me)
async def setalivetext(client: Client, message: Message):
    try:
        import PyroZen.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    Man = await edit_or_reply(message, "`Processing...`")
    if not text:
        return await edit_or_reply(
            message, "**Berikan Sebuah Text atau Reply ke text**"
        )
    sql.addgvar("ALIVE_TEKS_CUSTOM", text)
    await Man.edit(f"**Berhasil Mengcustom ALIVE TEXT Menjadi** `{text}`")
    restart()


@Client.on_message(filters.command("setemoji", cmd) & filters.me)
async def setemoji(client: Client, message: Message):
    try:
        import PyroZen.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    emoji = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    Man = await edit_or_reply(message, "`Processing...`")
    if not emoji:
        return await edit_or_reply(message, "**Berikan Sebuah Emoji**")
    sql.addgvar("ALIVE_EMOJI", emoji)
    await Man.edit(f"**Berhasil Mengcustom EMOJI ALIVE Menjadi** {emoji}")
    restart()
