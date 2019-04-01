import asyncio
from discord import Color, Embed
from utils import color


# Receiving the client from the main

client = None


def set_client(c):
    global client
    client = c

# Different logging types


async def info(text, chan=None, delete=True):
    """Displays an information in the terminal and if wanted also to the Discord channel."""
    pref = "[ " + color("INFO", "green") + " ]"
    terminal_text = ""
    if "`" in list(text):
        split = text.split("`")
        code = color(split[1], "code")
        split[1] = code
        terminal_text = "".join(split)
    output = pref + "  " + (text if terminal_text == "" else terminal_text)
    print(output.replace("*", ""))
    if chan != None:
        await send_chat(text, 0x2ecc71, chan, delete)


async def error(text, chan=None, delete=True):
    """Displays an error in the terminal and if wanted also to the Discord channel."""
    pref = "[ " + color("ERROR", "red") + " ]"
    terminal_text = ""
    if "`" in list(text):
        split = text.split("`")
        code = color(split[1], "code")
        split[1] = code
        terminal_text = "".join(split)
    output = pref + "  " + (text if terminal_text == "" else terminal_text)
    print(output.replace("*", ""))
    if chan != None:
        await send_chat(text, 0xe74c3c, chan, delete)


async def warn(text, chan=None, delete=True):
    """Displays a warning in the terminal and if wanted also to the Discord channel."""
    pref = "[ " + color("WARN", "yellow") + " ]"
    terminal_text = ""
    if "`" in list(text):
        split = text.split("`")
        code = color(split[1], "code")
        split[1] = code
        terminal_text = "".join(split)
    output = pref + "  " + (text if terminal_text == "" else terminal_text)
    print(output.replace("*", ""))
    if chan != None:
        await send_chat(text, 0xf1c40f, chan, delete)


# Sending the Embed chat message

async def send_chat(text, color, chan, delete):
    return_msg = await client.send_message(chan, embed=Embed(color=color, description=text))
    if delete:
        await asyncio.sleep(2.5)
        await client.delete_message(return_msg)
