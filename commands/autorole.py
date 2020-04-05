import Logger
import discord
from utils import db


async def ex(args, message, client, invoke):
    PREFIX = db.fetch_prefix(message.guild.id)
    args = [item.lower() for item in args]
    if message.author.id == message.guild.owner.id:
        if len(args) > 1:
            if args[0] == "add" and len(args) > 1:
                try:
                    role_id = int(args[1][3:-1])
                except ValueError:
                    await Logger.error("Please use **@role** and check if the role is mentionable.", chan=message.channel)
                    return
                found = message.guild.get_role(role_id)
                if found is not None:
                    if role_id not in db.fetch_autoroles(message.guild.id):
                        db.create_autorole(message.guild.id, role_id)
                        await Logger.info("Successfully added the role.", chan=message.channel)
                    else:
                        await Logger.error("Role is already registered.", chan=message.channel)
                else:
                    await Logger.error("Please use **@role** and check if the role is mentionable.", chan=message.channel)
            elif args[0] == "remove":
                role_id = args[1][3:-1]
                found = discord.utils.find(
                    lambda add: add.id == role_id, message.guild.roles)
                if found is not None:
                    if role_id in db.fetch_autoroles(message.guild.id):
                        db.delete_autorole(message.guild.id, role_id)
                        await Logger.info("Successfully removed the role.", chan=message.channel)
                    else:
                        await Logger.error("Role is not registered. Try **@role**", chan=message.channel)
                else:
                    await Logger.error("Please use **@role** and check if the role is mentionable.", chan=message.channel)
            else:
                await Logger.error("Usage: `%sautorole add/remove @role` or `%sautorole list`" % (PREFIX, PREFIX), chan=message.channel)
        elif len(args) < 1:
            await Logger.error("Usage: `%sautorole add/remove @role` or `%sautorole list`" % (PREFIX, PREFIX), chan=message.channel)
        elif args[0] == "list":
            role_names = []
            for r in db.fetch_autoroles(message.guild.id):
                found = discord.utils.find(
                    lambda add: add.id == r, message.author.guild.roles)
                if found is not None:
                    role_names.append("@" + found.name)
            if len(role_names) > 0:
                await Logger.info("Registered role(s): %s" % ", ".join(role_names))
                tmp = []
                for role_id in db.fetch_autoroles(message.guild.id):
                    tmp.append("<@&%s>" % role_id)
                out = ", ".join(tmp)
                await Logger.send_chat("Registered role(s): %s" % out, color=0x2ecc71, chan=message.channel, delete=False)
            else:
                await Logger.info("No roles registered, yet.", chan=message.channel)
    else:
        await Logger.error("This command is for GUILD OWNERS only!", chan=message.channel)
