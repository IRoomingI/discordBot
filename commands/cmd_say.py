import discord
from utils import log, stringify


async def ex(args, message, client, invoke):
    out = stringify(args)
    await client.delete_message(message)
    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description=(out)))
    log("Successfully said: '%s'" % out, "info")
