import discord, Logger


async def ex(args, message, client, invoke):
    args_out = ""
    args = " ".join(args)
    if len(args) > 0:
        args_out = "\n\nAttached arguments: %s" % args
    await client.send_message(message.author, embed=discord.Embed(color=discord.Color.blue(), description="Pong!" + args_out))
    await Logger.info("Successfully pinged Member: '%s'" % message.author.name)
