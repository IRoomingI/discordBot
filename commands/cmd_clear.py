import discord
import asyncio
from utils import log


async def ex(args, message, client, invoke):
    author = message.author.name
    channel = message.channel.__str__()[20:]
    if author != channel:
        try:
            ammount = int(args[0]) if len(args) > 0 else 2
        except():
            await log("Could not clear message(s)! Wrong value: '%s'" % args, "error", chat=True, chan=message.channel, client=client, delete=True)
            return

        messages = []
        async for m in client.logs_from(message.channel, limit=ammount):
            messages.append(m)

        try:
            await client.delete_messages(messages)
        except():
            await log("Can't delete messages older than 14 days.", "error", chat=True, chan=message.channel, client=client, delete=True)

        await log("Cleared %s messages" % (int(ammount) - 1 if int(ammount) <= 2 else 0), "info", chat=True, chan=message.channel, client=client, delete=True)
    else:
        await log("Can't delete direct messages!", "error", chat=True, chan=message.author, client=client)

