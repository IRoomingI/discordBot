import discord
import CONFIG
from logger import log
import asyncio

colorList = ["red", "green", "blue", "orange"]


def check(roles, args):
    for r in roles:
        if r.name == args:
            return r


def hasRole(message):
    out = []
    for r in message.author.roles:
        if r.name in colorList:
            out.append(r)
    return out


async def ex(args, message, client, invoke):
    roles = message.server.roles
    args = args.__str__()[1:-1].replace("'", "")
    args = args.__str__().replace(",", "")
    if not args == "help":
        oldrole = hasRole(message)
        role = check(roles, args)

        if role is not None:
            if len(oldrole) > 0:
                for r in oldrole:
                    await client.remove_roles(message.author, r)
            await asyncio.sleep(0.5)
            await client.add_roles(message.author, role)
        else:
            log("Couldn't change to color: '%s'" % args, "error")
            if len(args) > 0:
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(),
                                          description=("This color doesn't exist: *%s*. Type %scolor help" % (args, CONFIG.PREFIX))))
            else:
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(),
                                          description=("Type *%scolor help* to show all colors" % CONFIG.PREFIX)))
    elif args == "default" or args == "clear":
        roles = hasRole(message)
        if len(roles) > 0:
            for r in roles:
                await client.remove_roles(message.author, r)
    else:
        msg = "All colors: "
        for element in colorList:
            if element is not colorList[-1]:
                msg += element + ", "
            else:
                msg += element + ", default"

        await client.send_message(message.channel, msg)
