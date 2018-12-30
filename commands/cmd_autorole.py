import Logger, discord
from utils import data, config

async def ex(args, message, client, invoke):
    args = [item.lower() for item in args]
    if message.author.id == config["OWNER_ID"] or message.author.id == message.server.owner.id:
        if len(args) > 1:
            if args[0] == "add" and len(args)> 1:
                role_id = args[1][3:-1]
                if role_id not in data["AUTOROLE_IDS"]:
                    data["AUTOROLE_IDS"].append(role_id)
                    await Logger.info("Successfully added the role.", chat=True, chan=message.channel)
                else:
                    await Logger.error("Role is already registered.", chat=True, chan=message.channel)
            elif args[0] == "remove":
                role_id = args[1][3:-1]
                if role_id in data["AUTOROLE_IDS"]:
                    data["AUTOROLE_IDS"].remove(role_id)
                    await Logger.info("Successfully removed the role.", chat=True, chan=message.channel)
                else:
                    await Logger.error("Role is not registered. Try **@role**", chat=True, chan=message.channel)
        elif len(args) < 1:
            await Logger.error("Usage: `%sautorole add @role` or `%sautorole remove @role`" % (config["PREFIX"], config["PREFIX"]), chat=True, chan=message.channel)
        elif args[0] == "list":
            role_names = []
            for r in data["AUTOROLE_IDS"]:
                found = discord.utils.find(lambda add: add.id == r , message.author.server.roles)
                if found is not None:
                    role_names.append("@" + found.name)
            if len(role_names) > 0:
                await Logger.info("Registered role(s): %s" % ", ".join(role_names))
                tmp = []
                for id in data["AUTOROLE_IDS"]:
                    tmp.append("<@&%s>" % id)
                out = ", ".join(tmp)
                await Logger.send_chat("Registered role(s): %s" % out, color=0x2ecc71, chan=message.channel, delete=False)
            else:
                await Logger.info("No roles registered, yet.", chat=True, chan=message.channel)
    else:
        await Logger.error("This command is OWNER only!", chat=True, chan=message.channel)
