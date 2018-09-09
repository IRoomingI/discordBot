from utils import log, stringify


async def ex(args, message, client, invoke):
    args_out = ""
    args = stringify(args)
    if len(args) > 0:
        args_out = "\n\nAttached arguments: %s" % args
    await client.send_message(message.author, "Pong!" + args_out)
    await log("Successfully pinged Member: '%s'" % message.author.name, "info")
