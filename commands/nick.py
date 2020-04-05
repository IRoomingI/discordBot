import Logger


async def ex(args, message, client, invoke):
    if len(args) > 0:
        if args[0] == "remove" or args[0] == "clear":
            if message.author.id != message.guild.owner.id:
                await message.author.edit(nick=None)
                await Logger.info("Reset %s's nickname." % message.author.name)
            else:
                await Logger.error("Can't change the nick of the guild's owner.", chan=message.channel)
        else:
            nick = " ".join(args)
            if message.author.id != message.guild.owner.id:
                await message.author.edit(nick=nick)
                await Logger.info("Changed %s's nickname to %s." % (message.author.name, nick))
            else:
                await Logger.error("Can't change the nick of the guild's owner.", chan=message.channel)
    else:
        await Logger.error("No nickname entered.", chan=message.channel)
