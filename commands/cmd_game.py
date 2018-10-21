import discord, Logger
from utils import set_game


async def ex(args, message, client, invoke):
    out = " ".join(args)
    await client.change_presence(game=discord.Game(name=out))
    set_game(out)
    await Logger.info("Successfully changed game to: '%s'" % out)
