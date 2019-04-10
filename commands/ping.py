import discord
import Logger


async def ex(args, message, client, invoke):
    args_out = ""
    args = " ".join(args)
    if len(args) > 0:
        args_out = "\n\nAttached arguments: %s" % args
    await message.author.send(embed=discord.Embed(color=discord.Color.blue(), description="Pong!" + args_out))
    await Logger.info("Successfully pinged Member: '%s'" % message.author.name)
