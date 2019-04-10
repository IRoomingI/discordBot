import Logger
from utils import config


async def ex(args, message, client, invoke):
    if len(args) > 0:
        pref = str(args[0])
        if message.author.id == config.CONFIG["OWNER_ID"]:
            if len(pref) <= 8:
                config.CONFIG["PREFIX"] = pref
                await Logger.info("Successfully changed prefix to: **%s**" % pref, chan=message.channel, delete=False)
            else:
                await Logger.error("The prefix can't be longer than 8 characters.", chan=message.channel)
        else:
            await Logger.error("Failed because the user isn't the owner.", chan=message.channel)
    else:
        await Logger.error("Couldn't change prefix. Please enter a value.", chan=message.channel)
