# Credits Tomi Setiawan = @T0M1_X


import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from PyroZen.helpers.tools import get_arg
from PyroZen.modules.help import add_command_help


from pyrogram import Client, filters

 @Client.on_message(filters.command("copy", cmd) & filters.me)

# Define the copy command
@Client.on_message(filters.command("copy", cmd) & filters.me)
async def copy(client, Client, message: Message):
    # Extract the chat ID from the command link
    link_parts = message.text.split("/")
    try:
        chat_id = int(link_parts[-2])
    except (ValueError, IndexError):
        await message.reply("Invalid link provided.")
        return

    # Extract the message ID from the link
    try:
        message_id = int(link_parts[-1])
    except (ValueError, IndexError):
        await message.reply("Invalid link provided.")
        return

    # Copy the message to the specified chat
    try:
        copied_message = await client.copy_message(
            chat_id=chat_id,
            from_chat_id=message.chat.id,
            message_id=message_id
        )
        await message.reply("Message copied successfully.")
    except Exception as e:
        await message.reply(f"Failed to copy message: {e}")































