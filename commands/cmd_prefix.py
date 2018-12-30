import Logger
from utils import config


async def ex(args, message, client, invoke):
    if len(args) > 0:
        pref = str(args[0])
        if str(message.author.id) == config["OWNER_ID"]:
            if len(pref) <= 8:
                config["PREFIX"] = pref
                await Logger.info("Successfully changed prefix to: **%s**" % pref, chat=True, chan=message.channel, delete=False)
            else:
                await Logger.error("Longer than 8 characters.", chat=True, chan=message.channel)
        else:
            await Logger.error("Failed because the user isn't the owner.", chat=True, chan=message.channel)
    else:
        await Logger.error("Couldn't change prefix. Please enter a value.", chat=True, chan=message.channel)
