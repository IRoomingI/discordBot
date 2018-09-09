import discord
from utils import log, stringify, setGame


async def ex(args, message, client, invoke):
    out = stringify(args)
    await client.change_presence(game=discord.Game(name=out))
    setGame(out)
    log("Successfully changed game to: '%s'" % out, "info")
