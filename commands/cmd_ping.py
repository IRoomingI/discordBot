from utils import log

async def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = "\n\nAttached arguments: %s" % args.__str__()[1:-1].replace("'", "")
    await client.send_message(message.author, "Pong!" + args_out)
    log("Successfully pinged Member: '%s'" % message.author.name, "info")

