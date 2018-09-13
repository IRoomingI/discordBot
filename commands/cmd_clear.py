import discord
import asyncio
from utils import log


async def ex(args, message, client, invoke):
    author = message.author.name
    channel = message.channel.__str__()[20:]
    if author != channel:
        try:
            ammount = int(args[0]) if len(args) > 0 else 1
        except():
            await log("Could not clear message(s)! Wrong value: '%s'" % args, "error", chat=True, chan=message.channel, client=client, delete=True)
            return

        messages = []
        async for m in client.logs_from(message.channel, limit=ammount):
            messages.append(m)

        await client.delete_messages(messages)

        await log("Cleared %s messages" % ammount, "info", chat=True, chan=message.channel, client=client, delete=True)
    else:
        await log("Can't delete direct messages!", "error", chat=True, chan=message.author, client=client)

