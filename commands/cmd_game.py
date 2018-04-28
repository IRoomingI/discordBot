import discord
from logger import log

async def ex(args, message, client, invoke):
    args = args.__str__()[1:-1].replace("'", "")
    args = args.__str__().replace(",", "")
    await client.change_presence(game=discord.Game(name=args))
    log("Successfully changed game to: '%s'" % args, "info")
