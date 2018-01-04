import discord
import asyncio


async def ex(args, message, client, invoke):
    try:
        ammount = int(args[0]) + 1 if len(args) > 0 else 2
    except:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Please enter another value than %s" % ammount))
        return

    messages = []
    async for m in client.logs_from(message.channel, limit=ammount):
        messages.append(m)

    await client.delete_messages(messages)

    return_msg = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description="Cleared %s message(s)." % ammount))
    await asyncio.sleep(4)
    await client.delete_message(return_msg)
