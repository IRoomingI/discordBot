import discord, Logger
from utils import config


async def ex(args, message, client, invoke):
    out = " ".join(args)
    await client.change_presence(game=discord.Game(name=out))
    config["GAME"] = out
    await Logger.info("Successfully changed game to: '%s'" % out)
