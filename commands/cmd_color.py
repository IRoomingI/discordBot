import discord
import CONFIG
from logger import log
import asyncio

colorList = ["red", "green", "blue", "orange", "purple"]


def getNewRole(roles, args):
    for r in roles:
        if r.name == args:
            return r


def getOldRoles(message):
    out = []
    for r in message.author.roles:
        if r.name in colorList:
            out.append(r)
    return out


async def ex(args, message, client, invoke):
    roles = message.server.roles
    args = args.__str__()[1:-1].replace("'", "")
    args = args.__str__().replace(",", "")
    if args == "help":
        msg = "All colors: "
        for element in colorList:
            if element is not colorList[-1]:
                msg += element + ", "
            else:
                msg += element + ", default"

        await client.send_message(message.channel, msg)
        
    elif args == "default" or args == "clear":
        roles = getOldRoles(message)
        if len(roles) > 0:
            for r in roles:
                await client.remove_roles(message.author, r)
        log("Successfully cleared color!", "info")
    else:
        oldrole = getOldRoles(message)
        role = getNewRole(roles, args)

        if role is not None:
            if len(oldrole) > 0:
                for r in oldrole:
                    await client.remove_roles(message.author, r)
            await asyncio.sleep(0.5)
            await client.add_roles(message.author, role)
            log("Successfully changed to color: '%s'" % args, "info")
        else:
            log("Couldn't change to color: '%s'" % args, "error")
            if len(args) > 0:
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(),
                                          description=("This color doesn't exist: *%s*. Type %scolor help" % (args, CONFIG.PREFIX))))
            else:
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(),
                                          description=("Type *%scolor help* to show all colors" % CONFIG.PREFIX)))
        
