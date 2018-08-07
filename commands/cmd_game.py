import discord
from utils import log, stringify


async def ex(args, message, client, invoke):
    out = stringify(args)
    await client.change_presence(game=discord.Game(name=out))
    log("Successfully changed game to: '%s'" % out, "info")
