import discord
from utils import log, set_game


async def ex(args, message, client, invoke):
    out = " ".join(args)
    await client.change_presence(game=discord.Game(name=out))
    set_game(out)
    await log("Successfully changed game to: '%s'" % out, "info")
