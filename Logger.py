import asyncio
from discord import Color, Embed
from utils import paint


# Different logging types

color = paint.color


async def info(text, chan=None, delete=True):
    """Displays an information in the terminal and if wanted also to the Discord channel."""
    pref = "[ " + color("INFO", "green") + " ]"
    print(form(pref, text))
    if chan != None:
        await send_chat(text, 0x2ecc71, chan, delete)


async def error(text, chan=None, delete=True):
    """Displays an error in the terminal and if wanted also to the Discord channel."""
    pref = "[ " + color("ERROR", "red") + " ]"
    print(form(pref, text))
    if chan != None:
        await send_chat(text, 0xe74c3c, chan, delete)


async def warn(text, chan=None, delete=True):
    """Displays a warning in the terminal and if wanted also to the Discord channel."""
    pref = "[ " + color("WARN", "yellow") + " ]"
    print(form(pref, text))
    if chan != None:
        await send_chat(text, 0xf1c40f, chan, delete)

# Format the message

def form(pref, text):
    terminal_text = ""
    if "`" in list(text):
        split = text.split("`")
        code = color(split[1], "code")
        split[1] = code
        terminal_text = "".join(split)
    output = pref + "  " + (text if terminal_text == "" else terminal_text)
    return output.replace("*", "")


# Sending the Embed chat message

async def send_chat(text, color, chan, delete):
    await chan.send(embed=Embed(color=color, description=text), delete_after=2.5 if delete else None)
