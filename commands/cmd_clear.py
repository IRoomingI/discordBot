import discord
from utils import log, stringify


async def ex(args, message, client, invoke):
    author = message.author.name
    channel = str(message.channel)[20:]
    if author != channel:
        try:
            amount = int(args[0]) + 1 if len(args) > 0 and int(args[0]) >= 2 else 2
        except ValueError:
            await log("Could not clear message(s)! Wrong value: '%s'" % stringify(args), "error", chat=True, chan=message.channel, client=client)
            return

        messages = []
        async for m in client.logs_from(message.channel, limit=amount):
            messages.append(m)

        try:
            await client.delete_messages(messages)
        except discord.HTTPException:
            await log("Can't delete messages older than 14 days.", "error", chat=True, chan=message.channel, client=client)
        except discord.ClientException:
            await log("Can't delete more than 99 messages.", "error", chat=True, chan=message.channel, client=client)
    else:
        await log("Can't delete direct messages.", "error", chat=True, chan=message.author, client=client)
