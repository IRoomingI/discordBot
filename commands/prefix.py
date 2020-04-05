import Logger
from discord import Embed
from utils import db


async def ex(args, message, client, invoke):
    if len(args) > 0:
        if args[0] == "list":
            guild_prefix_dict = db.fetchall_prefix()
            embed = Embed(title="List of Prefixes", color=0x2ecc71)
            guilds = "\n".join(guild_prefix_dict.keys())
            embed.add_field(name="Guild", value=guilds)
            prefixes = ["**%s**" % prefix for prefix in guild_prefix_dict.values()]
            prefixes = "\n".join(prefixes)
            embed.add_field(name="Prefix", value=prefixes)
            await message.channel.send(embed=embed)
            await Logger.info("Successfully sent list of prefixes!")
        else:
            pref = str(args[0])
            if message.author.id == message.guild.owner.id:
                if len(pref) <= 8:
                    db.change_prefix(message.guild.id, pref)
                    await Logger.info("Successfully changed prefix to: **%s**" % pref, chan=message.channel, delete=False)
                else:
                    await Logger.error("The prefix can't be longer than 8 characters.", chan=message.channel)
            else:
                await Logger.error("Failed because the user isn't the guilds' owner.", chan=message.channel)
    else:
        await Logger.error("Couldn't change prefix. Please enter a value.", chan=message.channel)
