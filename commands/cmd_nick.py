import Logger
from utils import get_owner


async def ex(args, message, client, invoke):
    if len(args) > 0:
        if args[0] != "remove" or args[0] != "clear":
            nick = " ".join(args)
            if message.author.id != get_owner():
                await client.change_nickname(message.author, nick)
                await Logger.info("Changed %s's nickname to %s." % (message.author.name, nick))
            else:
                await Logger.error("Can't change the nick of the guilds owner.", chat=True, chan=message.channel)
        else:
            if message.author.id != get_owner():
                await client.change_nickname(message.author, None)
                await Logger.info("Reset %s's nickname." % message.author.name)
            else:
                await Logger.error("Can't change the nick of the guilds owner.", chat=True, chan=message.channel)
    else:
        await Logger.error("No nickname entered.", chat=True, chan=message.channel)
