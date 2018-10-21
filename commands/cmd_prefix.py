import Logger
from utils import set_prefix


async def ex(args, message, client, invoke):
    if len(args) > 0:
        await set_prefix(str(args[0]), message.channel, message.author.id, client)
    else:
        await Logger.error("Couldn't change prefix. Please enter a value.", chat=True, chan=message.channel)
