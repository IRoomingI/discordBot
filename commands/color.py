from utils import db
import discord
import Logger


def get_new_role(message, color):
    colorList = db.fetch_colors(message.guild.id)
    return message.guild.get_role(colorList[color])


def get_old_roles(message):
    out = []
    colorList = db.fetch_colors(message.guild.id)
    for r in message.author.roles:
        if r.id in colorList.values():
            out.append(r)
    return out


async def color_help(message, client):
    chan = message.channel
    color_list = db.fetch_colors(message.guild.id)
    PREFIX = db.fetch_prefix(message.guild.id)
    if len(color_list) > 0:
        msg = "All colors: "
        for name in color_list:
            msg += name + ", "
        msg += "default"
    else:
        msg = "No colors. Add with: `%scolor add color_name @role`" % PREFIX

    await Logger.info(msg, chan=chan, delete=False)


async def ex(args, message, client, invoke):
    roles = message.guild.roles
    color_list = db.fetch_colors(message.guild.id)
    PREFIX = db.fetch_prefix(message.guild.id)
    args = [item.lower() for item in args]
    if len(args) == 0 or args[0] == "help" or args[0] == "list":
        await color_help(message, client)
    elif args[0] == "default" or args[0] == "clear":
        roles = get_old_roles(message)
        if len(roles) > 0:
            for r in roles:
                await message.author.remove_roles(r)
        await Logger.info("Successfully cleared color.")
    elif args[0] == "add":
        if message.author.id == message.guild.owner.id:
            if len(args) > 2:
                color_name = args[1]
                try:
                    role_id = int(args[2][3:-1])
                except ValueError:
                    await Logger.error("Please use **@role** and check if the role is mentionable.", chan=message.channel)
                    return
                found = message.guild.get_role(role_id)
                if len(args[2]) > 20 and found is not None:
                    if color_name not in color_list:
                        db.create_color(message.guild.id, color_name, role_id)
                        await Logger.info("Successfully added color: '%s'" % color_name, chan=message.channel)
                    else:
                        await Logger.error("Color already exists: '%s'" % color_name, chan=message.channel)
                else:
                    await Logger.error("Please use **@role** and check if the role is mentionable.", chan=message.channel)
            else:
                await Logger.error("Usage: `%scolor add color_name @role`" % PREFIX, chan=message.channel)
        else:
            await Logger.error("Sorry, but only the owner can add colors.", chan=message.channel)
    elif args[0] == "remove":
        if message.author.id == message.guild.owner.id:
            if len(args) > 1:
                color_name = args[1]
                if color_name in color_list:
                    db.delete_color(message.guild.id,
                                    color_name, color_list[color_name])
                    await Logger.info("Successfully removed color: '%s'" % color_name, chan=message.channel)
                else:
                    await Logger.error("Color name doesn't exist: '%s'" % color_name, chan=message.channel)
            else:
                await Logger.error("Usage: `%scolor remove color_name`" % PREFIX, chan=message.channel)
        else:
            await Logger.error("Sorry, but only the owner can remove colors.", chan=message.channel)
    else:
        color = args[0]
        oldrole = get_old_roles(message)
        role = get_new_role(message, color)
        if role is None:
            if len(color) > 0:
                await Logger.error("Couldn't change to color because it doesn't exist: '%s'" % color, chan=message.channel)
            else:
                await color_help(message.channel, client)
        else:
            try:
                await message.author.add_roles(role)
            except discord.Forbidden:
                await Logger.error("Can't add the new color role. No permission.", chan=message.channel)
            if len(oldrole) > 0:
                for r in oldrole:
                    try:
                        await message.author.remove_roles(r)
                    except discord.Forbidden:
                        await Logger.error("Can't remove your old color role: **%s**. No permission." % r.name, chan=message.channel)
            await Logger.info("Successfully changed to color: '%s'" % color)
