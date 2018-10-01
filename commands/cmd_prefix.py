import discord
import asyncio
from utils import setPrefix, log

async def ex(args, message, client, invoke):
    if len(args) > 0:
        await setPrefix(str(args[0]), message.channel, message.author.id, client=client)
    else:
        await log("Couldn't change prefix. Please enter a value.", "error", chat=True, client=client, chan=message.channel)