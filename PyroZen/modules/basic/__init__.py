import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "PyroZen"])

async def join(client):
    try:
        await client.join_chat("ZennXSupport")
        await client.join_chat("DuniaVirtualMenfess")
        await client.join_chat("Dunia_VirtualZ")
    except BaseException:
        pass
