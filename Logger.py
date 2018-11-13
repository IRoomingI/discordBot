import asyncio
from discord import Color, Embed
from utils import color


# Receiving the client from the main

client = None

def set_client(c):
    global client
    client = c

# Different logging types

async def info(text, chat=False, chan=None, delete=True):
    """Displays an information in the terminal and if wanted also to the Discord channel."""
    pref = "[ " + color("INFO", "green") + " ]"
    output = pref + "  " + text
    print(output.replace("*", ""))
    if chat: await send_chat(text, 0x2ecc71, chan, delete)


async def error(text, chat=False, chan=None, delete=True):
    """Displays an error in the terminal and if wanted also to the Discord channel."""
    pref = "[ " + color("ERROR", "red") + " ]"
    output = pref + "  " + text
    print(output.replace("*", ""))
    if chat: await send_chat(text, 0xe74c3c, chan, delete)


async def warn(text, chat=False, chan=None, delete=True):
    """Displays a warning in the terminal and if wanted also to the Discord channel."""
    pref = "[ " + color("WARN", "yellow") + " ]"
    output = pref + "  " + text
    print(output.replace("*", ""))
    if chat: await send_chat(text, 0xf1c40f, chan, delete)


# Sending the Embed chat message
async def send_chat(text, color, chan, delete):
    return_msg = await client.send_message(chan, embed=Embed(color=color, description=text))
    if delete:
        await asyncio.sleep(2.5)
        await client.delete_message(return_msg) 