import discord
import Logger
from utils import config, db


async def ex(args, message, client, invoke):
    if len(args) >= 2:
        act_type = args[0].lower()
        activity = " ".join(args[1:])
        if act_type == "game":
            await client.change_presence(activity=discord.Game(name=activity))
            config.CONFIG["ACTIVITY"] = {"GAME": activity}
        if act_type == "streaming":
            await client.change_presence(activity=discord.Streaming(name=activity))
            config.CONFIG["ACTIVITY"] = {"STREAMING": activity}
        if act_type == "custom":
            await client.change_presence(activity=discord.CustomActivity(name=activity))
            config.CONFIG["ACTIVITY"] = {"CUSTOM": activity}

        await Logger.info("Successfully set activity (%s) to: '%s'" % (act_type, activity))
    else:
        PREFIX = db.fetch_prefix(message.guild.id)
        await Logger.error("Usage: `%sactivity <game/streaming/custom> text`" % PREFIX)