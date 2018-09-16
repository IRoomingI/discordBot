from utils import log, stringify
import discord

async def ex(args, message, client, invoke):
    args_out = ""
    args = stringify(args)
    if len(args) > 0:
        args_out = "\n\nAttached arguments: %s" % args
    await client.send_message(message.author, embed=discord.Embed(color=discord.Color.blue(), description="Pong!" + args_out))
    await log("Successfully pinged Member: '%s'" % message.author.name, "info")
