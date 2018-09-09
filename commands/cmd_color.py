import discord
from utils import log, getPrefix
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


def colorHelp():
    msg = "All colors: "
    for element in colorList:
        if element is not colorList[-1]:
            msg += element + ", "
        else:
            msg += element + ", default"

    log(msg, "info", chat=True, channel=message.channel)

async def ex(args, message, client, invoke):
    roles = message.server.roles
    args = args[0]
    if args == "help":
        colorHelp()
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
            if len(args) > 0:
                log("Couldn't change to color because it doesn't exist: '%s'" % args, "error", chat=True, channel=message.channel)
            else:
                colorHelp()
