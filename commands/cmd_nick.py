from utils import log, stringify, getOwner


async def ex(args, message, client, invoke):
    if len(args) > 0:
        if args[0] != "remove" or args[0] != "clear":
            nick = stringify(args)
            if message.author.id != getOwner():
                await client.change_nickname(message.author, nick)
                await log("Changed %s's nickname to %s" % (message.author.name, nick), "info")
            else:
                await log("Can't change the nick of the guilds owner", "error", chat=True, chan=message.channel, client=client, delete=True)
        else:
            if message.author.id != getOwner():
                await client.change_nickname(message.author, None)
                await log("Reset %s's nickname" % message.author.name, "info")
            else:
                await log("Can't change the nick of the guilds owner", "error", chat=True, chan=message.channel, client=client, delete=True)
    else:
        await log("No nickname entered", "error", chat=True, chan=message.channel, client=client, delete=True)