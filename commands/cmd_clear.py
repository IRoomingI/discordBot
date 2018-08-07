import discord
import asyncio
from utils import log


async def ex(args, message, client, invoke):
    author = message.author.name
    channel = message.channel.__str__()[20:]
    if author != channel:
        try:
            ammount = int(args[0]) + 1 if len(args) > 0 else 2
        except:
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Please enter another value than '%s'" % ammount))
            log("Could not clear message(s)! Wrong value: '%s'" % args, "error")
            return

        messages = []
        async for m in client.logs_from(message.channel, limit=ammount):
            messages.append(m)

        await client.delete_messages(messages)

        return_msg = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description="Cleared %s message(s)." % ammount))
        await asyncio.sleep(3)
        await client.delete_message(return_msg)
    else:
        await client.send_message(message.author, embed=discord.Embed(color=discord.Color.red(), description="Can't delete direct messages!"))
        log("Could not clear message(s)!", "error")
