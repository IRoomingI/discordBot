import Logger, discord
from utils import get_autorole_ids, set_autorole_ids, get_prefix

async def ex(args, message, client, invoke):
    autorole_ids = get_autorole_ids()
    args = [item.lower() for item in args]
    if len(args) > 1:
        if args[0] == "add" and len(args)> 1:
            role_id = args[1][3:-1]
            if role_id not in autorole_ids:
                autorole_ids.append(role_id)
                set_autorole_ids(autorole_ids)
                await Logger.info("Successfully added the role.", chat=True, chan=message.channel)
            else:
                await Logger.error("Role is already registered.", chat=True, chan=message.channel)
        elif args[0] == "remove":
            role_id = args[1][3:-1]
            if role_id in autorole_ids:
                autorole_ids.remove(role_id)
                set_autorole_ids(autorole_ids)
                await Logger.info("Successfully removed the role.", chat=True, chan=message.channel)
            else:
                await Logger.error("Role is not registered. Try **@role**", chat=True, chan=message.channel)
    elif len(args) < 1:
        await Logger.error("Usage: `%sautorole add @role` or `%sautorole remove @role`" % (get_prefix(), get_prefix()), chat=True, chan=message.channel)
    elif args[0] == "list":
        role_names = []
        for r in autorole_ids:
            found = discord.utils.find(lambda add: add.id == r , message.author.server.roles)
            if found is not None:
                role_names.append("@" + found.name)
        if len(role_names) > 0:
            await Logger.info("Registered role(s): %s" % ", ".join(role_names), chat=True, chan=message.channel, delete=False)
        else:
            await Logger.info("No roles registered, yet.", chat=True, chan=message.channel)
