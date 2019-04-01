from utils import config
import discord
import asyncio
import Logger
import db


def get_new_role(message, color):
    roles = message.server.roles
    colorList = db.fetch_colors(message.server.id)
    for r in roles:
        if r.id == colorList[color]:
            return r


def get_old_roles(message):
    out = []
    colorList = db.fetch_colors(message.server.id)
    for r in message.author.roles:
        for color in colorList:
            if r.id in colorList[color]:
                out.append(r)
    return out


async def color_help(message, client):
    chan = message.channel
    color_list = db.fetch_colors(message.server.id)
    if len(color_list) > 0:
        msg = "All colors: "
        count = 1
        for key in color_list:
            if count < len(color_list):
                msg += key + ", "
            else:
                msg += key + ", default"
            count += 1
    else:
        msg = "No colors. Add with: `%scolor add color_name @role`" % config["PREFIX"]

    await Logger.info(msg, chan=chan, delete=False)


async def ex(args, message, client, invoke):
    roles = message.server.roles
    color_list = db.fetch_colors(message.server.id)
    args = [item.lower() for item in args]
    if len(args) == 0 or args[0] == "help" or args[0] == "list":
        await color_help(message, client)
    elif args[0] == "default" or args[0] == "clear":
        roles = get_old_roles(message)
        if len(roles) > 0:
            for r in roles:
                await client.remove_roles(message.author, r)
        await Logger.info("Successfully cleared color.")
    elif args[0] == "add":
        if message.author.id == config["OWNER_ID"] or message.author.id == message.server.owner.id:
            if len(args) > 2:
                color_name = args[1]
                role_id = args[2][3:-1]
                found = discord.utils.find(
                    lambda add: add.id == role_id, message.server.roles)
                if len(args[2]) > 20 and found != None:
                    if color_name not in color_list:
                        db.create_color(message.server.id, color_name, role_id)
                        await Logger.info("Successfully added color: '%s'" % color_name, chan=message.channel)
                    else:
                        await Logger.error("Color already exists: '%s'" % color_name, chan=message.channel)
                else:
                    await Logger.error("Please use **@role** and check if the role is mentionable.", chan=message.channel)
            else:
                await Logger.error("Usage: `%scolor add color_name @role`" % config["PREFIX"], chan=message.channel)
        else:
            await Logger.error("Sorry, but only the owner can add colors.", chan=message.channel)
    elif args[0] == "remove":
        if message.author.id == config["OWNER_ID"]:
            if len(args) > 1:
                color_name = args[1]
                if color_name in color_list:
                    db.delete_color(message.server.id,
                                    color_name, color_list[color_name])
                    await Logger.info("Successfully removed color: '%s'" % color_name, chan=message.channel)
                else:
                    await Logger.error("Color name doesn't exist: '%s'" % color_name, chan=message.channel)
            else:
                await Logger.error("Usage: `%scolor remove color_name`" % config["PREFIX"], chan=message.channel)
        else:
            await Logger.error("Sorry, but only the Owner can remove colors.", chan=message.channel)
    else:
        color = args[0]
        oldrole = get_old_roles(message)
        try:
            role = get_new_role(message, color)
        except KeyError:
            if len(color) > 0:
                await Logger.error("Couldn't change to color because it doesn't exist: '%s'" % color, chan=message.channel)
            else:
                await color_help(message.channel, client)
        else:
            if len(oldrole) > 0:
                for r in oldrole:
                    try:
                        await client.remove_roles(message.author, r)
                    except discord.Forbidden:
                        await Logger.error("Can't remove your old color role: **%s**. No permission." % r, chan=message.channel)
            await asyncio.sleep(0.5)
            try:
                await client.add_roles(message.author, role)
            except discord.Forbidden:
                await Logger.error("Can't add the new color role. No permission.", chan=message.channel)
            await Logger.info("Successfully changed to color: '%s'" % color)
