import discord
import CONFIG
from logger import log

colorList = ["red", "green", "blue", "orange"]


async def ex(args, message, client, invoke):
    roles = message.server.roles
    args = args.__str__()[1:-1].replace("'", "")
    args = args.__str__().replace(",", "")
    if not args == "help":
        oldrole = hasRole(message)
        role = check(roles, args)

        if(role is not None):
            await client.add_roles(message.author, role)
        else:
            log("Couldn't change to color: '%s'" % args, "error")
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(),
                                      description=("This color doesn't exist: %s. Type %scolor help" % (args, CONFIG.PREFIX))))
        if(oldrole is not None):
            await client.remove_roles(message.author, oldrole)
    else:
        msg = "All colors: "
        for element in colorList:
            if element is not colorList[-1]:
                msg += element + ", "
            else:
                msg += element

        await client.send_message(message.channel, msg)


def check(roles, args):
    for r in roles:
        if r.name == args:
            return r


def hasRole(message):
    for r in message.author.roles:
        if r.name in colorList:
            return r
