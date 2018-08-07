import discord
from logger import log

async def ex(args, message, client, invoke):
    out = ""
    for word in args:
        out += word + " "
    await client.change_presence(game=discord.Game(name=out))
    log("Successfully changed game to: '%s'" % args, "info")
