from utils import log, get_colors, set_colors, get_prefix, get_owner
import discord
import asyncio


def get_new_role(roles, color):
    colorList = get_colors()
    for r in roles:
        if r.id == colorList[color]:
            return r


def get_old_roles(message):
    out = []
    colorList = get_colors()
    for r in message.author.roles:
        for color in colorList:
            if r.id in colorList[color]:
                out.append(r)
    return out


async def color_help(chan, client):
    colorList = get_colors()
    msg = "All colors: "
    count = 1
    for key in colorList:
        if count < len(colorList):
            msg += key + ", "
        else:
            msg += key + ", default"
        count += 1

    await log(msg, "info", chat=True, chan=chan, client=client, delete=False)


async def ex(args, message, client, invoke):
    roles = message.server.roles
    args = [item.lower() for item in args]
    if len(args) == 0 or args[0] == "help" or args[0] == "list":
        await color_help(message.channel, client)
    elif args[0] == "default" or args[0] == "clear":
        roles = get_old_roles(message)
        if len(roles) > 0:
            for r in roles:
                await client.remove_roles(message.author, r)
        await log("Successfully cleared color.", "info")
    elif args[0] == "add":
        if message.author.id == get_owner():
            if len(args) > 1:
                color_name = args[1]
                if len(args) > 2:
                    if len(args[2]) > 20:
                        role_id = args[2][3:-1]
                        if color_name not in get_colors():
                            roles = get_colors()
                            roles.update({color_name: role_id})
                            set_colors(roles)
                            await log("Successfully added color: '%s'" % color_name, "info", chat=True, chan=message.channel, client=client)
                    else:
                        await log("Please use **@role** and check if the role is mentionable.", "error", chat=True, chan=message.channel, client=client)
                else:
                    await log("Usage: %scolor add color_name @role" % get_prefix(), "error", chat=True, chan=message.channel, client=client)
            else:
                await log("Usage: %scolor add color_name @role" % get_prefix(), "error", chat=True, chan=message.channel, client=client)
        else:
            await log("Sorry, but only the Owner can add colors.", "error", chat=True, chan=message.channel, client=client)
    elif args[0] == "remove":
        if message.author.id == get_owner():
            if len(args) > 1:
                color_name = args[1]
                if color_name in get_colors():
                    roles = get_colors()
                    del roles[color_name]
                    set_colors(roles)
                    await log("Successfully removed color: '%s'" % color_name, "info", chat=True, chan=message.channel, client=client)
                else:
                    await log("Color name doesn't exist: '%s'" % color_name, "error", chat=True, chan=message.channel, client=client)
            else:
                await log("Usage: %scolor remove color_name" % get_prefix(), "error", chat=True, chan=message.channel, client=client)    
        else:
            await log("Sorry, but only the Owner can remove colors.", "error", chat=True, chan=message.channel, client=client)
    else:
        color = args[0]
        oldrole = get_old_roles(message)
        try:
            role = get_new_role(roles, color)
        except KeyError:
            if len(color) > 0:
                await log("Couldn't change to color because it doesn't exist: '%s'" % color, "error", chat=True, chan=message.channel, client=client)
            else:
                await color_help(message.channel, client)
        else:
            if len(oldrole) > 0:
                for r in oldrole:
                    try:
                        await client.remove_roles(message.author, r)
                    except discord.Forbidden:
                        await log("Can't remove your old color role: **%s**. No permission." % r, "error", chat=True, chan=message.channel, client=client)
            await asyncio.sleep(0.5)
            try:
                await client.add_roles(message.author, role)
            except discord.Forbidden:
                        await log("Can't add the new color role. No permission.", "error", chat=True, chan=message.channel, client=client)
            await log("Successfully changed to color: '%s'" % color, "info")
            
