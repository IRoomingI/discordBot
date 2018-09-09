import discord
import asyncio
from utils import setPrefix, log

async def ex(args, message, client, invoke):
    setPrefix(args[0], message.channel, message.User.id)