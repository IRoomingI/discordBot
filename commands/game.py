import discord
import Logger
from utils import config


async def ex(args, message, client, invoke):
    out = " ".join(args)
    await client.change_presence(activity=discord.Game(name=out))
    config.CONFIG["GAME"] = out
    await Logger.info("Successfully changed game to: '%s'" % out)
