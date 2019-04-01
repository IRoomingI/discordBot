import discord
import Logger


async def ex(args, message, client, invoke):
    author = message.author.name
    channel = str(message.channel)[20:]
    if author != channel:
        try:
            amount = int(args[0]) + \
                1 if len(args) > 0 and int(args[0]) >= 2 else 2
        except ValueError:
            await Logger.error("Could not clear message(s)! Wrong value: '%s'" % " ".join(args), chan=message.channel)
            return

        try:
            await client.purge_from(message.channel, limit=amount)
        except discord.HTTPException:
            await Logger.error("Can't delete messages older than 14 days.", chan=message.channel)
        except discord.ClientException:
            await Logger.error("Can't delete more than 99 messages.", chan=message.channel)
    else:
        await Logger.error("Can't delete direct messages.", chan=message.author)
