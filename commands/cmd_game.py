import discord
from utils import log, stringify, set_game


async def ex(args, message, client, invoke):
    out = stringify(args)
    await client.change_presence(game=discord.Game(name=out))
    set_game(out)
    await log("Successfully changed game to: '%s'" % out, "info")
